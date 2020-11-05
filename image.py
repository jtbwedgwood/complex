import cmath
import math
import tkinter

from PIL import Image, ImageTk

def num_to_HSL(z):
    return (

        # Hue
        cmath.phase(z),

        # Saturation
        1,

        # Lightness
        2 * math.atan(abs(z)) / math.pi
    )

def HSL_to_RGB(hsl):

    # Borrowed from Wikipedia
    hue, saturation, lightness = hsl
    chroma = (1 - abs(2 * lightness - 1)) * saturation
    h_prime = hue * 3 / math.pi
    X = chroma * (1 - abs(h_prime % 2 - 1))
    if h_prime == 0:
        zeroed = (0, 0, 0)
    elif h_prime <= 1:
        zeroed = (chroma, X, 0)
    elif h_prime <= 2:
        zeroed = (X, chroma, 0)
    elif h_prime <= 3:
        zeroed = (0, chroma, X)
    elif h_prime <= 4:
        zeroed = (0, X, chroma)
    elif h_prime <= 5:
        zeroed = (X, 0, chroma)
    else:
        zeroed = (chroma, 0, X)
    m = lightness - chroma / 2
    return (color + m for color in zeroed)

class CGraph:

    # TODO user-specified color function
    def __init__(self, width, height, origin_coords=None, scale=2, function=None):
        self.width = width
        self.height = height
        self.origin_coords = origin_coords

        # Default value for origin_coords is in terms of other initial variables
        if self.origin_coords is None:
            self.origin_coords = (width / 2, height / 2)
        self.scale = scale
        self.function = function

        # Default function is identically zero
        if self.function is None:
            self.function = lambda x: return 0

    def generate_array(self):

        # Generate grid of points on which to apply function
        step_size =  self.scale / self.width
        top_left = complex(-1 * self.scale * self.origin_coords[0] / self.width, self.scale * self.origin_coords[1] / self.height)
        points_grid = [
            [

                # Points separated by step_size in both x and y direction
                complex(top_left[0] + x * step_size, top_left[1] + y * step_size)
                for x in range(self.width)
            ]
            for y in range(self.height)
        ]

        # Apply function to each point
        return [[self.function(point) for point in row] for row in points_grid]
    def generate_image(self):
        im = Image.fromarray(self.generate_array(), mode="RGB")
        return im
