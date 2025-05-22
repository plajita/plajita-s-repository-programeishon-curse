# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
def calc(): 
    n1=float(entry_num1.get())
    n2=float(entry_num2.get())
    op = entry_op.get()
    result = (eval(f"{n1} + {op} + {n2}"))
    label_result.configure(f"result:{result}")
    print(n1)
    print(n2)

#crear ventana

root = tk.Tk()
root.minsize(500,300)

#Elements

#label

label_title = ttk.Label(root, text="calculator")
label_result = ttk.Label(root, text="resultado")

#texbox

text_num1 = tk.StringVar()
text_num2 = tk.StringVar()
text_op = tk.StringVar()

#Entry

entry_num1 = ttk.Entry(root,width=20,textvariable=text_num1)                                          
entry_num2 = ttk.Entry(root,width=20,textvariable=text_num2)                                                                
entry_op = ttk.Entry(root,width=20,textvariable=text_op)                                                                

 #button

button = tk.Button(root,text="calcular",command=calc)

#positions

label_title.grid(column=0,row=0)
entry_num1.grid(column=1,row=1)
entry_num2.grid(column=1,row=2)
button.grid(column=1,row=40)
entry_op.grid(column=3,row=79)

#iniciar ventana

root.mainloop()



