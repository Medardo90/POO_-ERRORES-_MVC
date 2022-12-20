# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:43:07 2022

@author: lab
"""

import tkinter as tk 
from tkinter import messagebox
class MyException(Exception):
    pass
class View(): 
    def __init__(self, root, model):
        self.model = model
        self.root = root
        self.star_widgets()
    def star_widgets(self):
        self.frame = tk.Frame(self.root)
        
        self.nombre = tk.StringVar()
        self.precio = tk.IntVar()
        
        self.label_mail= tk.Label(self.root, text="e-mail")
        self.label_ci= tk.Label(self.root, text="precio")
        self.e1= tk.Entry(self.root,textvariable= self.nombre, font =("Arial",14))
        self.e2= tk.Entry(self.root,textvariable= self.precio, font =("Arial",14))
        self.b1= tk.Button(self.root,text="agregar", conmand =self.agregardatos)
        self.label_resp = tk.Label(self.root)
        
        self.label_mail.grid(row = 1, column= 0)
        self.label_ci.grid(row = 1, column= 0)
        self.e1.grid(row=0 , column= 1)
        self.e2.grid(row=1 , column= 1)
        self.b1.grid(row=2 , column= 1)
        self.label_resp.grid(row = 3, column= 1)
        
        self.datos=[]
        