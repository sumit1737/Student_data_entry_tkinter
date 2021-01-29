from os import path
from tkinter import *
from tkinter import ttk
import json

class DispCrs():
    def __init__(self,window,wid,hg):
        self.rt = window
        self.width = wid
        self.height = hg
        self.shwCrsBttn = None
        # #################################################
        proj_folder = path.dirname(__file__)
        data_folder = path.join(proj_folder,'data')
        self.dataFile = path.join(data_folder,"Course.json") # File to save the data in        
    
    def makeTable(self):
        self.my_tree = ttk.Treeview(self.rt)
        
        #DEFINE COLUMNS
        colTup = ("CourseID","CourseName")
        self.my_tree['columns'] = colTup
        
        #FORMAT COLUMNS
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("CourseID",anchor=W,width=int(0.25*(self.width/2)),minwidth=75)
        self.my_tree.column("CourseName",anchor=E,width=int(0.75*(self.width/2)))
        
        # CREATE HEADINGS
        #self.my_tree.heading("#0", text="",anchor=W)
        for i in range(0,len(colTup)):
            anch = CENTER
            self.my_tree.heading(colTup[i],text=colTup[i],anchor=anch)        
    
    
    def fillTable(self):# reading the JSON file and filling the data in the table
        
        x = self.my_tree.get_children() # Deleting all the entries before we reload the tree
        if x != '()':
            for child in x:
                self.my_tree.delete(child)
        
        # reading the JSON file and filling the data in the table
        fl = ""
        try:
            fl = open(self.dataFile,"r")
        except IOError:
            mssg = messagebox.showerror('Error','JSON data file not found')
            return
        data = json.load(fl)
        lst = data["Courses"]
        
        for i in range(0,len(lst)):
            self.my_tree.insert(parent='', index='end', iid=i, text="", values=(lst[i]["CourseID"],lst[i]["CourseName"]))
        
    def shwStd(self):
        # FILLING DATA
        self.fillTable()
        
    def shwBttn(self):
        # Event functions handling the color of the show students button
        def on_enter(e):
            self.shwCrsBttn['activebackground'] = "black"
            self.shwCrsBttn["activeforeground"] = "white"
        def on_click(e):
            self.shwCrsBttn['activebackground'] = "white"
            self.shwCrsBttn["activeforeground"] = "black"      
        def on_release(e):
            self.shwCrsBttn['activebackground'] = "black"
            self.shwCrsBttn["activeforeground"] = "white"        
        
        
        self.shwCrsBttn = Button(self.rt, text="Show Courses", bg="black",fg="white",command=self.shwStd)
        self.shwCrsBttn.bind('<Enter>',on_enter)
        self.shwCrsBttn.bind('<Button-1>',on_click)
        self.shwCrsBttn.bind('<ButtonRelease-1>',on_release)
        self.shwCrsBttn.place(relx=0.5,rely=0.8,anchor=CENTER)    
    
    def table(self):
        # MAKING THE TABLE
        self.makeTable()
        
        # FILLING DATA
        self.shwBttn()
        
        # DISPLAY TABLE 
        self.my_tree.pack()