"""Minimal executable anchor for the ResNet residual block.

This stub is not a full training system. It exists to bind the paper's
residual formulation to executable code in the ARA physical layer.
"""

from __future__ import annotations

import torch
from torch import Tensor, nn


class ResidualBlock(nn.Module):
    """Two-layer residual block for the 18/34-layer ResNet family.

    Args:
        in_channels: Input channel count.
        out_channels: Output channel count.
        stride: Spatial stride applied by the first convolution.
    """

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1) -> None:
        super().__init__()
        self.branch = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
        )
        if stride != 1 or in_channels != out_channels:
            self.shortcut: nn.Module = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels),
            )
        else:
            self.shortcut = nn.Identity()
        self.activation = nn.ReLU(inplace=True)

    def forward(self, x: Tensor) -> Tensor:
        """Return `relu(F(x) + shortcut(x))` for an input of shape `[B, C, H, W]`."""
        residual: Tensor = self.branch(x)
        skip: Tensor = self.shortcut(x)
        return self.activation(residual + skip)
