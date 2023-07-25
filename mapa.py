import tkinter
from tkinter import messagebox
import tkintermapview

# Función que puede mostrar información sobre el punto del mapa que hayan creado
def mostrar_info(info):
    messagebox.showinfo('mapa', info)


root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")

root_tk.title("mapa.py")

# Luego de importar la librería tkintermapview creamos un objeto mapa 

map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
# Lo ubicamos en nuestra ventana por medio de place (se puede usar pack o grid también)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Generamos una posición céntrica 
map_widget.set_position(-24.789124241917268, -65.41029074730143) 

# Generamos un zoom predeterminado
map_widget.set_zoom(16)

# Vamos a generar unos puntos de ejemplo, esto se puede hacer con un método que consulte a nuestro json
map_widget.set_marker(-24.786182651664653, -65.40902474474923, text='Hotel Almería', command= lambda x, infor='Hotel 4 estrellas centrico': mostrar_info(infor))
map_widget.set_marker(-24.789650214280968, -65.40883162571583, text='Hotel Marilian', command= lambda x, infor='Hotel para viajeros': mostrar_info(infor))
map_widget.set_marker(-24.792942361005093, -65.41099885042385, text='Hotel Alejandro 1', command= lambda x, infor='Hotel 5 estrellas centrico': mostrar_info(infor))
map_widget.set_marker(-24.788208655075884, -65.40533402544452, text='Hotel Ayres de Salta', command= lambda x, infor='Hotel con buena gastronomía': mostrar_info(infor))


root_tk.mainloop()