import tkinter as tk
from canvas import ClaseCanvas

root = tk.Tk()

frame = tk.Frame(root, width=800, height=600)
frame.pack()

clase_canvas = ClaseCanvas(frame)


root.mainloop()
