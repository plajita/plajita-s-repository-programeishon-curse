# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
def calc(): 
    velocidad=float(entry_velocidad.get())
    tiempo=float(entry_tiempo.get())
    #op = entry_op.get()
    #result = (eval(f"{n1} + {op} + {n2}"))
    distancia = velocidad * tiempo
    label_result.configure(text=f"distancia recorrida en metros:{distancia}")
    

#crear ventana

root = tk.Tk()
root.minsize(500,300)

#Elements

#label

label_title = ttk.Label(root, text="calculator")
label_result = ttk.Label(root, text="resultado")

#texbox

text_velocidad = tk.StringVar()
text_tiempo = tk.StringVar()
#text_op = tk.StringVar()

#Entry

entry_velocidad = ttk.Entry(root,width=20,textvariable=text_velocidad)                                          
entry_tiempo = ttk.Entry(root,width=20,textvariable=text_tiempo)                                                                
#entry_op = ttk.Entry(root,width=20,textvariable=text_op)                                                                

 #button

button = tk.Button(root,text="calcular",command=calc)

#positions

label_title.grid(column=0,row=0)
entry_velocidad.grid(column=1,row=1)
entry_tiempo.grid(column=1,row=2)
button.grid(column=1,row=4)
label_result.grid(column=0,row=5)
#entry_op.grid(column=3,row=79)

#iniciar ventana

root.mainloop()







