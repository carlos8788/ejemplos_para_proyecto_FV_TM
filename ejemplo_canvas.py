import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

frame = tk.Frame(root, width=800, height=600)
frame.pack()

canvas = tk.Canvas(frame, width=800, height=450)
canvas.pack()

img = Image.open('salta.png')
background_image = ImageTk.PhotoImage(img)

canvas.create_image(0, 0, anchor='nw', image=background_image)
canvas.image = background_image

button1 = tk.Button(
    frame,
    text='Button 1',
    borderwidth=0,
    relief='ridge',
    width=16,
    bg='blue',
    foreground='white',
    font='Arial 16'
)
canvas.create_window(200, 400, window=button1)

button2 = tk.Button(
    frame,
    text='Button 2',
    borderwidth=0,
    relief='ridge',
    width=16,
    bg='blue',
    foreground='white',
    font='Arial 16'
)
canvas.create_window(400, 400, window=button2)

button3 = tk.Button(
    frame,
    text='Button 3',
    borderwidth=0,
    relief='ridge',
    width=16,
    bg='blue',
    foreground='white',
    font='Arial 16'
)
canvas.create_window(600, 400, window=button3)

root.mainloop()
