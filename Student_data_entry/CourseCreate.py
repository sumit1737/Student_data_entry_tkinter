from os import path
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import json
from tkinter.filedialog import asksaveasfile

class nCourse():
    def __init__(self,window,wid,hg):
        self.rt = window
        self.width = wid
        self.height = hg
        self.eCrsId = ""
        self.eCrsName = ""
        # ############################
        proj_folder = path.dirname(__file__)
        data_folder = path.join(proj_folder,'data')
        self.dataFile = path.join(data_folder,"Course.json") # File to save the data in
        
    def labels(self):
        fntStyle = tkFont.Font(size=12)
        lblList = []
        lblList.append(Label(self.rt,text="Course ID",font=fntStyle))
        lblList.append(Label(self.rt,text="Course Name",font=fntStyle))
        
        self.eCrsId = Entry(self.rt,width=int(self.width/23.4))
        self.eCrsName = Entry(self.rt,width=int(self.width/23.4))        
        
        
        #position variables
        yOffset = self.height/4.8 #80
        interval = self.height/4.8 
        xoff = self.width/2826.206896552 #m0.29
        
        self.eCrsId.place(anchor=NE, relx=0.8, y = yOffset)
        self.eCrsName.place(anchor=NE, relx=0.8, y = yOffset + interval)        
        
        for i in range(len(lblList)):
            lblList[i].place(anchor=NE, relx = xoff, y = (yOffset + (i * interval)))
    
    def wrtInJson(self,data,flName):
        with open(flName,'w') as f: 
            json.dump(data, f, indent=4)    
        
    def saveFile(self):
        msgBox = messagebox.showinfo("Save","Course Added")
            
        ##Saving the records in Student.json
        nstds = {
            "CourseID": self.eCrsId.get(),
            "CourseName": self.eCrsName.get()
        }
        
        fl = ""
        try:
            fl = open(self.dataFile,"r")
            details = json.load(fl)
            temp = details["Courses"]
            temp.append(nstds)
            self.wrtInJson(details,self.dataFile)
            
        except IOError:
            fl = open(self.dataFile,"w")
            d = {
                "Courses":[nstds]}
            json.dump(d,fl,indent=4)
        fl.close()

        
        
    def clearInput(self):
        self.eCrsId.delete(0,'end')
        self.eCrsName.delete(0,'end')
        
    def svBttnHvr(self,e):
        self.svBtnLabel.config(text="Save course",borderwidth=2,relief="ridge")
        self.svBtnLabel.place(anchor=NE,relx=0.35,y=int(self.height/1.28)+25)
    def svBttnLv(self,e):
        self.svBtnLabel.config(text="",borderwidth=0,relief="flat")
        self.svBtnLabel.place(anchor=NE,relx=0,y=int(self.height/1.28)+25)
    
    def bttns(self):
        saveBttn = Button(self.rt,text="Save",command=self.saveFile,width=15)
        self.svBtnLabel = Label(self.rt,text=None)
        saveBttn.bind('<Enter>',self.svBttnHvr)
        saveBttn.bind('<Leave>',self.svBttnLv)
        clearBttn = Button(self.rt,text="Clear",command=self.clearInput,width=15)
        
        
        clearBttn.place(anchor=NE,relx=0.8,y=int(self.height/1.28))
        saveBttn.place(anchor=NE,relx=0.4,y=int(self.height/1.28))    
        
        
