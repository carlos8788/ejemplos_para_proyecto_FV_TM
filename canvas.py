import tkinter as tk
from PIL import Image, ImageTk

class ClaseCanvas:
    def __init__(self, frame):
        self.frame = frame
        self.canvas = tk.Canvas(self.frame, width=800, height=450)
        self.canvas.pack()

        self.img = Image.open('salta.png')
        self.background_image = ImageTk.PhotoImage(self.img)

        self.canvas.create_image(0, 0, anchor='nw', image=self.background_image)
        self.canvas.image = self.background_image

        self.button1 = tk.Button(
            self.frame,
            text='Button 1',
            borderwidth=0,
            relief='ridge',
            width=16,
            bg='blue',
            foreground='white',
            font='Arial 16'
        )
        self.canvas.create_window(200, 400, window=self.button1)

        self.button2 = tk.Button(
            self.frame,
            text='Button 2',
            borderwidth=0,
            relief='ridge',
            width=16,
            bg='blue',
            foreground='white',
            font='Arial 16'
        )
        self.canvas.create_window(400, 400, window=self.button2)

        self.button3 = tk.Button(
            self.frame,
            text='Button 3',
            borderwidth=0,
            relief='ridge',
            width=16,
            bg='blue',
            foreground='white',
            font='Arial 16'
        )
        self.canvas.create_window(600, 400, window=self.button3)