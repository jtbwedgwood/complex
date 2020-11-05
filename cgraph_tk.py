import tkinter as tk

from cgraph import *
from PIL import ImageTk

window = tk.Tk()
cg = CGraph(x_range=(-30,30), y_range=(-20,20), function=lambda z: np.sin(z))
im = cg.generate_image()
im_tk = ImageTk.PhotoImage(im)
label = tk.Label(window, image=im_tk)
label.pack()
window.mainloop()
