import numpy as np
import tkinter as tk

from PIL import Image, ImageTk
from utilities import num_to_HSL, HSL_to_RGB

class CGraph:
    def __init__(self, width=300, height=200, x_range=(-3,3), y_range=(-2,2), function=None, color_by="HSL"):
        self.width = width
        self.height = height
        self.x_range = self.x_min, self.x_max = x_range
        self.y_range = self.y_min, self.y_max = y_range
        self.function = function

        # Default function is identically zero
        if self.function is None:
            self.function = lambda z: z
        self.color_by = color_by
        if self.color_by == "HSL":
            self.color_function = num_to_HSL
        else:
            raise ValueError("Unsupported value for parameter color_by.")

    def generate_array(self):
        return np.array(
            [
                [self.function(x + y * 1j) for x in np.linspace(self.x_min, self.x_max, self.width)]
                for y in np.linspace(self.y_min, self.y_max, self.height)[::-1]
            ]
        )

    def generate_image(self):
        arr = self.generate_array()
        color_array = np.array(
            [
                [HSL_to_RGB(self.color_function(elem)) for elem in row]
                for row in arr
            ]
        )
        im = Image.fromarray(color_array, mode="RGB")
        return im

# class CGraphTk:
