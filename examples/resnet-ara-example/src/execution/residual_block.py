"""Residual building blocks from He et al. 2015.

Implements the basic 2-layer block (Fig. 2) and the 3-layer bottleneck block
(Fig. 5 right) with identity (Option A) and projection (Option B/C) shortcuts.

Only the novel residual-block contribution is shown here: stems, stage stacking,
and heads are deferred to a higher-level model file.
"""

from typing import Literal, Optional

import torch
from torch import Tensor, nn


ShortcutOption = Literal["A", "B", "C"]


def _conv3x3(in_c: int, out_c: int, stride: int = 1) -> nn.Conv2d:
    return nn.Conv2d(in_c, out_c, kernel_size=3, stride=stride, padding=1, bias=False)


def _conv1x1(in_c: int, out_c: int, stride: int = 1) -> nn.Conv2d:
    return nn.Conv2d(in_c, out_c, kernel_size=1, stride=stride, bias=False)


class _IdentityWithZeroPad(nn.Module):
    """Option A shortcut: stride-2 sample on spatial axes, zero-pad new channels."""

    def __init__(self, in_c: int, out_c: int, stride: int) -> None:
        super().__init__()
        if out_c < in_c:
            raise ValueError("Option A only widens channels; never narrows them.")
        self.stride = stride
        self.extra = out_c - in_c

    def forward(self, x: Tensor) -> Tensor:
        if self.stride > 1:
            x = x[:, :, :: self.stride, :: self.stride]
        if self.extra > 0:
            pad = x.new_zeros(x.size(0), self.extra, x.size(2), x.size(3))
            x = torch.cat([x, pad], dim=1)
        return x


def _build_shortcut(
    in_c: int,
    out_c: int,
    stride: int,
    option: ShortcutOption,
) -> nn.Module:
    if in_c == out_c and stride == 1 and option != "C":
        return nn.Identity()
    if option == "A":
        return _IdentityWithZeroPad(in_c, out_c, stride)
    return nn.Sequential(_conv1x1(in_c, out_c, stride), nn.BatchNorm2d(out_c))


class BasicBlock(nn.Module):
    """ResNet basic block — used in ResNet-18 / ResNet-34."""

    expansion: int = 1

    def __init__(
        self,
        in_channels: int,
        channels: int,
        stride: int = 1,
        shortcut: ShortcutOption = "A",
    ) -> None:
        super().__init__()
        out_channels = channels * self.expansion
        self.conv1 = _conv3x3(in_channels, channels, stride=stride)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = _conv3x3(channels, out_channels, stride=1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.shortcut = _build_shortcut(in_channels, out_channels, stride, shortcut)

    def forward(self, x: Tensor) -> Tensor:
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out = out + self.shortcut(x)
        return self.relu(out)


class BottleneckBlock(nn.Module):
    """ResNet bottleneck block — used in ResNet-50 / ResNet-101 / ResNet-152.

    Layout: 1x1 (reduce) -> 3x3 -> 1x1 (restore). The expansion factor 4 means
    the output of the block is 4 * `channels` channels deep (Fig. 5 right).
    """

    expansion: int = 4

    def __init__(
        self,
        in_channels: int,
        channels: int,
        stride: int = 1,
        shortcut: ShortcutOption = "B",
    ) -> None:
        super().__init__()
        out_channels = channels * self.expansion
        self.conv1 = _conv1x1(in_channels, channels)
        self.bn1 = nn.BatchNorm2d(channels)
        # Stride lives on the 3x3 conv — matches the original He et al. design.
        self.conv2 = _conv3x3(channels, channels, stride=stride)
        self.bn2 = nn.BatchNorm2d(channels)
        self.conv3 = _conv1x1(channels, out_channels)
        self.bn3 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.shortcut = _build_shortcut(in_channels, out_channels, stride, shortcut)

    def forward(self, x: Tensor) -> Tensor:
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.relu(self.bn2(self.conv2(out)))
        out = self.bn3(self.conv3(out))
        out = out + self.shortcut(x)
        return self.relu(out)


def make_stage(
    block: type[nn.Module],
    in_channels: int,
    channels: int,
    blocks: int,
    stride: int,
    shortcut: ShortcutOption,
) -> nn.Sequential:
    """Stack `blocks` residual blocks; first block handles down-sampling."""
    layers: list[nn.Module] = [
        block(in_channels, channels, stride=stride, shortcut=shortcut)
    ]
    in_c = channels * block.expansion  # type: ignore[attr-defined]
    for _ in range(1, blocks):
        layers.append(block(in_c, channels, stride=1, shortcut=shortcut))
    return nn.Sequential(*layers)


# Per-depth stage layouts from Table 1.
RESNET_LAYOUTS: dict[str, tuple[type[nn.Module], tuple[int, int, int, int]]] = {
    "resnet18": (BasicBlock, (2, 2, 2, 2)),
    "resnet34": (BasicBlock, (3, 4, 6, 3)),
    "resnet50": (BottleneckBlock, (3, 4, 6, 3)),
    "resnet101": (BottleneckBlock, (3, 4, 23, 3)),
    "resnet152": (BottleneckBlock, (3, 8, 36, 3)),
}
