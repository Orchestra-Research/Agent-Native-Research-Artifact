"""Residual block implementations for ResNet.

Implements the basic 2-layer block (ResNet-18/34) and the 3-layer
bottleneck block (ResNet-50/101/152) as described in He et al. 2015.
"""

import torch
import torch.nn as nn
from typing import Optional


class BasicBlock(nn.Module):
    """2-layer residual block: 3x3 conv -> BN -> ReLU -> 3x3 conv -> BN + shortcut -> ReLU.

    Used in ResNet-18 and ResNet-34.
    """

    expansion: int = 1

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        stride: int = 1,
        downsample: Optional[nn.Module] = None,
    ) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(
            in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False
        )
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(
            out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False
        )
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.downsample = downsample

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity  # F(x) + x
        out = self.relu(out)
        return out


class BottleneckBlock(nn.Module):
    """3-layer bottleneck block: 1x1 -> 3x3 -> 1x1 with shortcut.

    Used in ResNet-50, ResNet-101, and ResNet-152.
    The 1x1 layers reduce and restore dimensions, making the 3x3 layer
    a bottleneck with smaller input/output dimensions.
    """

    expansion: int = 4

    def __init__(
        self,
        in_channels: int,
        bottleneck_channels: int,
        stride: int = 1,
        downsample: Optional[nn.Module] = None,
    ) -> None:
        super().__init__()
        out_channels = bottleneck_channels * self.expansion

        # 1x1 reduce
        self.conv1 = nn.Conv2d(in_channels, bottleneck_channels, kernel_size=1, bias=False)
        self.bn1 = nn.BatchNorm2d(bottleneck_channels)

        # 3x3 convolution
        self.conv2 = nn.Conv2d(
            bottleneck_channels, bottleneck_channels, kernel_size=3, stride=stride, padding=1, bias=False
        )
        self.bn2 = nn.BatchNorm2d(bottleneck_channels)

        # 1x1 restore
        self.conv3 = nn.Conv2d(bottleneck_channels, out_channels, kernel_size=1, bias=False)
        self.bn3 = nn.BatchNorm2d(out_channels)

        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        identity = x

        out = self.conv1(x)       # reduce
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)      # 3x3
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)      # restore
        out = self.bn3(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity  # F(x) + x
        out = self.relu(out)
        return out
