"""Training recipe for ImageNet and CIFAR-10 ResNets (He et al. 2015, §3.4 & §4.2).

This file captures the *recipe*, not a runnable trainer: optimizer construction,
LR schedule (including the 110-layer CIFAR warmup), and the BN-after-conv
convention. Higher-level data loaders, distributed wrappers, and logging are
intentionally omitted.
"""

from dataclasses import dataclass
from typing import Iterable

import torch
from torch import nn
from torch.optim import SGD


@dataclass(frozen=True)
class ImageNetRecipe:
    """ImageNet recipe from §3.4."""

    batch_size: int = 256
    initial_lr: float = 0.1
    momentum: float = 0.9
    weight_decay: float = 1e-4
    max_iter: int = 600_000          # "up to 60 x 10^4"
    lr_decay_factor: float = 0.1     # divide by 10 on plateau
    use_dropout: bool = False        # explicitly off (BN replaces it)


@dataclass(frozen=True)
class CifarRecipe:
    """CIFAR-10 recipe from §4.2."""

    batch_size: int = 128
    initial_lr: float = 0.1
    momentum: float = 0.9
    weight_decay: float = 1e-4
    max_iter: int = 64_000
    lr_drop_iters: tuple[int, int] = (32_000, 48_000)
    lr_decay_factor: float = 0.1
    # Warmup applies only to the 110-layer (n=18) ResNet (footnote 5):
    warmup_lr: float = 0.01
    warmup_until_train_err: float = 0.80   # restore initial_lr when train err < 80%


def build_optimizer(
    params: Iterable[nn.Parameter],
    recipe: ImageNetRecipe | CifarRecipe,
) -> SGD:
    """SGD with momentum + weight decay, matching the paper."""
    return SGD(
        params,
        lr=recipe.initial_lr,
        momentum=recipe.momentum,
        weight_decay=recipe.weight_decay,
    )


def imagenet_lr(it: int, current_lr: float, plateau: bool, recipe: ImageNetRecipe) -> float:
    """ImageNet LR rule: drop by 10x whenever validation error plateaus.

    The caller supplies the plateau signal — typically derived from a moving
    average of validation error.
    """
    if plateau:
        return current_lr * recipe.lr_decay_factor
    return current_lr


def cifar_lr(
    it: int,
    train_err: float,
    needs_warmup: bool,
    recipe: CifarRecipe,
) -> float:
    """Fixed step schedule for CIFAR-10 with optional 110-layer warmup.

    Args:
        it: current iteration (0-indexed).
        train_err: latest training error in [0, 1].
        needs_warmup: True only for the 110-layer (n=18) ResNet (§4.2, footnote 5).
        recipe: CIFAR recipe.
    """
    if needs_warmup and train_err >= recipe.warmup_until_train_err:
        return recipe.warmup_lr
    lr = recipe.initial_lr
    for drop_iter in recipe.lr_drop_iters:
        if it >= drop_iter:
            lr *= recipe.lr_decay_factor
    return lr


def msra_init(module: nn.Module) -> None:
    """MSRA / Kaiming-normal init for conv weights (He et al. 2015, ref [13])."""
    for m in module.modules():
        if isinstance(m, nn.Conv2d):
            nn.init.kaiming_normal_(m.weight, mode="fan_out", nonlinearity="relu")
        elif isinstance(m, nn.BatchNorm2d):
            nn.init.constant_(m.weight, 1.0)
            nn.init.constant_(m.bias, 0.0)


def freeze_bn_stats(model: nn.Module) -> None:
    """Freeze BN running stats — used for Faster R-CNN fine-tuning (Appendix A)."""
    for m in model.modules():
        if isinstance(m, nn.BatchNorm2d):
            m.eval()
            for p in m.parameters():
                p.requires_grad = False
