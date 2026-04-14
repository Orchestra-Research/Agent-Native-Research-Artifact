"""Minimal residual block implementations for ResNet (He et al., 2016).

Implements the core novel contribution: identity shortcut connections
that enable training of very deep networks without degradation.
"""

import torch
import torch.nn as nn
from typing import Optional


class BasicBlock(nn.Module):
    """Two-layer residual block for ResNet-18/34 (§3.1, Figure 2).

    y = F(x, {W1, W2}) + x
    F = W2 * ReLU(BN(W1 * x))
    """

    expansion: int = 1

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        stride: int = 1,
        shortcut: Optional[nn.Module] = None,
    ) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, 3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, 3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.shortcut = shortcut

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        identity = x

        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))

        if self.shortcut is not None:
            identity = self.shortcut(x)

        out += identity
        out = self.relu(out)
        return out


class BottleneckBlock(nn.Module):
    """Three-layer bottleneck block for ResNet-50/101/152 (§4.1, Figure 5).

    1x1 (reduce) -> 3x3 (spatial) -> 1x1 (restore) + shortcut
    """

    expansion: int = 4

    def __init__(
        self,
        in_channels: int,
        bottleneck_channels: int,
        stride: int = 1,
        shortcut: Optional[nn.Module] = None,
    ) -> None:
        super().__init__()
        out_channels = bottleneck_channels * self.expansion
        self.conv1 = nn.Conv2d(in_channels, bottleneck_channels, 1, bias=False)
        self.bn1 = nn.BatchNorm2d(bottleneck_channels)
        self.conv2 = nn.Conv2d(bottleneck_channels, bottleneck_channels, 3, stride=stride, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(bottleneck_channels)
        self.conv3 = nn.Conv2d(bottleneck_channels, out_channels, 1, bias=False)
        self.bn3 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.shortcut = shortcut

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        identity = x

        out = self.relu(self.bn1(self.conv1(x)))
        out = self.relu(self.bn2(self.conv2(out)))
        out = self.bn3(self.conv3(out))

        if self.shortcut is not None:
            identity = self.shortcut(x)

        out += identity
        out = self.relu(out)
        return out
