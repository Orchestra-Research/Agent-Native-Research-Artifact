"""Minimal training-recipe anchor for the ResNet ImageNet slice.

This module is intentionally small. It exists so training heuristics and
configuration references point to executable objects rather than empty paths.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class SgdRecipe:
    batch_size: int = 256
    initial_lr: float = 0.1
    momentum: float = 0.9
    weight_decay: float = 1e-4
    max_iterations: int = 600_000
    use_dropout: bool = False


@dataclass(frozen=True)
class ImagenetAugmentation:
    resize_shorter_side_range: Tuple[int, int] = (256, 480)
    crop_size: Tuple[int, int] = (224, 224)
    horizontal_flip: bool = True
    mean_subtraction: str = "per_pixel"
    color_augmentation: str = "standard"


def lr_schedule_description() -> str:
    """Return the schedule stated in the paper for the ImageNet recipe."""
    return "Start at 0.1 and divide by 10 when error plateaus."
