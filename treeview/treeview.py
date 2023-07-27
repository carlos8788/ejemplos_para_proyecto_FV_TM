import tkinter as tk
from tkinter import ttk
from data import Data

datos_json = Data('ubicaciones.json')
lista_datos = datos_json.load_from_json()

def agregar(treeview, dato_1, dato_2, dato_3, dato_4):
    treeview.insert('', 'end', values=(dato_1, dato_2, dato_3, dato_4))
    diccionario = {
        "id": int(dato_1),
        "direccion": dato_2,
        "coordenadas": [
            dato_3,
            dato_4
        ]
    }
    lista_datos.append(diccionario)
    datos_json.save_to_json(lista_datos)

def eliminar_datos(tabla):
        item = tabla.focus()
        # global lista_datos
        ubicacion = tabla.item(item)['values']
        id = ubicacion[0]
        for i in lista_datos:
             if i['id'] == id:
                  lista_datos.remove(i)

        tabla.delete(item)
        datos_json.save_to_json(lista_datos)
            

root = tk.Tk()
root.geometry('1000x600')

data_1 = tk.StringVar()
data_2 = tk.StringVar()
data_3 = tk.StringVar()
data_4 = tk.StringVar()


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

# label_5 = tk.Label(frame_1, text='Dato 5')
# label_5.grid(row=4, column=0)
# entry_5 = tk.Entry(frame_1, textvariable=data_5)
# entry_5.grid(row=4, column=1, ipadx=30, pady=15)

button = tk.Button(frame_1, text='Agregar', command=lambda: agregar(tree, data_1.get(), data_2.get(), data_3.get(), data_4.get()))
button.grid(row=5, column=0, columnspan=2, ipadx=60, pady=15)

button2 = tk.Button(frame_1, text='Borrar', command=lambda: eliminar_datos(tree))
button2.grid(row=6, column=0, columnspan=2, ipadx=60, pady=15)

# TABLA
tree = ttk.Treeview(root, columns=('A', 'B', 'C', 'D'), show='headings')

# DEFINIMOS EL NOMBRE DE CADA CAMPO Y LO REFERENCIAMOS
tree.heading('A', text='ID')
tree.heading('B', text='Direccion')
tree.heading('C', text='lat')
tree.heading('D', text='Long')
# tree.heading('E', text='Campo 5')

# CON INSERT, vamos a insertar los valores según corresponda, como guía vean que el primer elemento de values se ubica en la primer columna y así sucesivamente
for i in lista_datos:
    tree.insert('', 'end', values=(i['id'], i['direccion'], i['coordenadas'][0], i['coordenadas'][1]))


tree.grid(row=6, column=0)

root.mainloop()
