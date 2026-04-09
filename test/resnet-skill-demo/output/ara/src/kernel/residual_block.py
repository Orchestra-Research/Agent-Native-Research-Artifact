"""Minimal executable anchor for a ResNet basic block.

This is a compact implementation anchor for the paper slice represented by
the artifact. It is not intended to reproduce the full training system.
"""

from __future__ import annotations

import torch
from torch import Tensor, nn


class BasicResidualBlock(nn.Module):
    """Two-layer residual block with an optional shortcut projection."""

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1) -> None:
        super().__init__()
        self.residual = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
        )

        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels),
            )
        else:
            self.shortcut = nn.Identity()

        self.activation = nn.ReLU(inplace=True)

    def forward(self, x: Tensor) -> Tensor:
        y = self.residual(x) + self.shortcut(x)
        return self.activation(y)

