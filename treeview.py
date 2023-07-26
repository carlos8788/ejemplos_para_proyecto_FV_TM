import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# TABLA
tree = ttk.Treeview(root, columns=('A', 'B', 'C', 'D', 'E'), show='headings')

# DEFINIMOS EL NOMBRE DE CADA CAMPO Y LO REFERENCIAMOS
tree.heading('A', text='Campo 1')
tree.heading('B', text='Campo 2')
tree.heading('C', text='Campo 3')
tree.heading('D', text='Campo 4')
tree.heading('E', text='Campo 5')

# CON INSERT, vamos a insertar los valores según corresponda, como guía vean que el primer elemento de values se ubica en la primer columna y así sucesivamente
for i in range(10):
    tree.insert('', 'end', values=(f'Dato {i+1}A', f'Dato {i+1}B', f'Dato {i+1}C', f'Dato {i+1}D', f'Dato {i+1}E'))


tree.grid(row=0, column=0)

root.mainloop()
