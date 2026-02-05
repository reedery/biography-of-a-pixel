from __future__ import annotations

import numpy as np


class Display:
    """Frame buffer plus drawing functions."""

    def __init__(self, resolution: int) -> None:
        self.resolution = resolution
        self.ss_level = 1
        self._reset_buffer()

    def _reset_buffer(self) -> None:
        render_res = self.resolution * self.ss_level
        self.buffer = np.zeros((render_res, render_res, 3), dtype=np.uint8)

    def set_supersampling(self, ss_level: int) -> None:
        self.ss_level = max(1, int(ss_level))
        self._reset_buffer()

    def _set_pixel(self, x: int, y: int, color: tuple[int, int, int]) -> None:
        if 0 <= y < self.buffer.shape[0] and 0 <= x < self.buffer.shape[1]:
            self.buffer[y, x] = color

    def draw_line(
        self, x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int]
    ) -> None:
        """Bresenham's algorithm"""
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy

        while True:
            self._set_pixel(x0, y0, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def draw_polygon(
        self, points: list[tuple[int, int]], color: tuple[int, int, int]
    ) -> None:
        """Draw a closed polygon."""
        return

    def downsample(self) -> np.ndarray:
        """Downsamples to logical resolution when SSAA is active."""
        if self.ss_level <= 1:
            return self.buffer
        res = self.resolution
        ss_level = self.ss_level
        return (
            self.buffer.reshape(res, ss_level, res, ss_level, 3)
            .mean(axis=(1, 3))
            .astype(np.uint8)
        )
