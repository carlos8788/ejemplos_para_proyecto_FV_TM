from tkinter import Tk, Button, Label, StringVar
from controller import PersonaController
class MiApp:
    def __init__(self):
        root = Tk()
        root.geometry('600x500')
        persona = PersonaController()
        var_text = StringVar()
        var_text.set(persona.ver_personas())
        label = Label(text=var_text.get())
        label.pack()
        button = Button(root, text='mostar persona')
        button.pack()

        root.mainloop()
    
