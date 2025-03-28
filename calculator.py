# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:36:58 2025

@author: Nehal_Jain
"""



import tkinter as tk


    
def add():
    try:
        a=int(e1.get())
        b=int(e2.get())
       
        result=a+b
        L2.config(text=f"Result: {result}")
    except ValueError:
        L2.config(text="Please enter valid numbers.")
        
def sub():
    try:
        a=int(e1.get())
        b=int(e2.get())
       
        result=a-b
        L2.config(text=f"Result: {result}")
    except ValueError:
        L2.config(text="Please enter valid numbers.")
        
def mul():
    try:
        a=int(e1.get())
        b=int(e2.get())
       
        result=a*b
        L2.config(text=f"Result: {result}")
    except ValueError:
        L2.config(text="Please enter valid numbers.")
        
        
def div():
    try:
        a=int(e1.get())
        b=int(e2.get())
       
        result=a/b
        L2.config(text=f"Result: {result}")
    except ValueError:
        L2.config(text="Please enter valid numbers.")
    
    
root=tk.Tk()
root.title("Calc")
L1=tk.Label(root,text="Calculator", font=('Times New Roman',20,'bold'))
L1.pack()

L3=tk.Label(root,text="First number : ", font=('Times New Roman',12,'bold'))
L3.pack()
e1=tk.Entry(root)
e1.pack(pady=10)

L4=tk.Label(root,text="Second number : ", font=('Times New Roman',12,'bold'))
L4.pack()
e2=tk.Entry(root)
e2.pack(padx=100,pady=10)


b1=tk.Button(root,text="Addition",command=add)
b2=tk.Button(root,text="Subtraction",command=sub)
b3=tk.Button(root,text="Multiplication",command=mul)
b4=tk.Button(root,text="Divison",command=div)
b1.pack()
b2.pack()
b3.pack()
b4.pack()

L2=tk.Label(root,text="Result :", font=('Times New Roman',12,'bold'))
L2.pack()

root.mainloop()