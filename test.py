from cgraph import *
from utilities import *
import numpy as np

# cg = CGraph(x_range=(-30,30), y_range=(-20,20), function=lambda z: np.sin(z))
# im = cg.generate_image()
# im.show()

print(parse_string_as_function("z + 1")(1))
