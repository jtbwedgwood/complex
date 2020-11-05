import numpy as np

def num_to_HSL(z):

    # Borrowed from Wikipedia
    return (
        np.angle(z) % (2 * np.pi),
        1,
        2 * np.arctan(abs(z)) / np.pi
    )

def HSL_to_RGB(hsl):
    hue, saturation, lightness = hsl
    chroma = (1 - abs(2 * lightness - 1)) * saturation
    h_prime = hue * 3 / np.pi
    X = chroma * (1 - abs(h_prime % 2 - 1))
    if h_prime == 0:
        zeroed = [0, 0, 0]
    elif h_prime <= 1:
        zeroed = [chroma, X, 0]
    elif h_prime <= 2:
        zeroed = [X, chroma, 0]
    elif h_prime <= 3:
        zeroed = [0, chroma, X]
    elif h_prime <= 4:
        zeroed = [0, X, chroma]
    elif h_prime <= 5:
        zeroed = [X, 0, chroma]
    else:
        zeroed = [chroma, 0, X]
    m = lightness - chroma / 2
    return [(255 * (color + m)).astype(np.uint8) for color in zeroed]

def parse_string_as_function(str):
    return lambda z: eval(str)
