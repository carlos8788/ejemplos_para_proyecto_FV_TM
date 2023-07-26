import tkinter as tk
from tkinter import ttk


def agregar(treeview, dato_1, dato_2, dato_3, dato_4, dato_5):
    treeview.insert('', 'end', values=(dato_1, dato_2, dato_3, dato_4, dato_5))

root = tk.Tk()
root.geometry('1000x600')

data_1 = tk.StringVar()
data_2 = tk.StringVar()
data_3 = tk.StringVar()
data_4 = tk.StringVar()
data_5 = tk.StringVar()

frame_1 = tk.Frame(root)
frame_1.grid(row=0, column=0)

label_1 = tk.Label(frame_1, text='Dato 1')
label_1.grid(row=0, column=0)
entry_1 = tk.Entry(frame_1, textvariable=data_1)
entry_1.grid(row=0, column=1, ipadx=30, pady=15)

label_2 = tk.Label(frame_1, text='Dato 2')
label_2.grid(row=1, column=0)
entry_2 = tk.Entry(frame_1, textvariable=data_2)
entry_2.grid(row=1, column=1, ipadx=30, pady=15)

label_3 = tk.Label(frame_1, text='Dato 3')
label_3.grid(row=2, column=0)
entry_3 = tk.Entry(frame_1, textvariable=data_3)
entry_3.grid(row=2, column=1, ipadx=30, pady=15)

label_4 = tk.Label(frame_1, text='Dato 4')
label_4.grid(row=3, column=0)
entry_4 = tk.Entry(frame_1, textvariable=data_4)
entry_4.grid(row=3, column=1, ipadx=30, pady=15)

label_5 = tk.Label(frame_1, text='Dato 5')
label_5.grid(row=4, column=0)
entry_5 = tk.Entry(frame_1, textvariable=data_5)
entry_5.grid(row=4, column=1, ipadx=30, pady=15)

button = tk.Button(frame_1, text='Agregar', command=lambda: agregar(tree, data_1.get(), data_2.get(), data_3.get(), data_4.get(), data_5.get()))
button.grid(row=5, column=0, columnspan=2, ipadx=60, pady=15)

# TABLA
tree = ttk.Treeview(root, columns=('A', 'B', 'C', 'D', 'E'), show='headings')

# DEFINIMOS EL NOMBRE DE CADA CAMPO Y LO REFERENCIAMOS
tree.heading('A', text='Campo 1')
tree.heading('B', text='Campo 2')
tree.heading('C', text='Campo 3')
tree.heading('D', text='Campo 4')
tree.heading('E', text='Campo 5')

# CON INSERT, vamos a insertar los valores según corresponda, como guía vean que el primer elemento de values se ubica en la primer columna y así sucesivamente
for i in range(5):
    tree.insert('', 'end', values=(f'Dato {i+1}A', f'Dato {i+1}B', f'Dato {i+1}C', f'Dato {i+1}D', f'Dato {i+1}E'))


tree.grid(row=6, column=0)

root.mainloop()
