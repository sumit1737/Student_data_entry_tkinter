from os import path
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import json

class nStudent(): # ENTERING THE DATA OF THE NEW STUDENT
    def __init__(self,window,wid,hg):
        self.rt = window # Parent element of the tab
        self.width = wid
        self.height = hg
        # Widgets in the tab #########
        self.eyName = ""
        self.eyRll = ""
        self.chGender = ""
        self.AoC = ""
        self.phN = ""
        self.yrB = ""
        self.Hstl = ""
        self.svBtnLabel = ""
        # ############################
        proj_folder = path.dirname(__file__)
        data_folder = path.join(proj_folder,'data')
        self.dataFile = path.join(data_folder,"Student.json") # File to save the data in
    
    def labels(self):
        
        # drawing the labels on the left side of the screen
        fntStyle = tkFont.Font(size=12)
        lblList = []
        lblList.append(Label(self.rt,text="Enter Your Name",font=fntStyle))
        lblList.append(Label(self.rt,text="Enter Your Rollno",font=fntStyle))
        lblList.append(Label(self.rt,text="Choose Your Gender",font=fntStyle))
        lblList.append(Label(self.rt,text="Address of Correspondence",font=fntStyle))
        lblList.append(Label(self.rt,text="Phone No",font=fntStyle))
        lblList.append(Label(self.rt,text="Your Batch",font=fntStyle))
        lblList.append(Label(self.rt,text="Hostel[Y/N]",font=fntStyle))
        
        
        
        # Widgets for taking input #################
        self.eyName = Entry(self.rt,width=int(self.width/23.4)) # name widget
        self.eyRll = Entry(self.rt,width=int(self.width/23.4)) # roll number
        
        # gender
        self.chGender = StringVar()
        self.radioMl = Radiobutton(self.rt, text="Male", variable=self.chGender, value="Male")
        self.radioFml = Radiobutton(self.rt, text="Female", variable=self.chGender, value="Female")
        self.chGender.set(0)

        
        self.AoC = Entry(self.rt,width=int(self.width/23.4)) # address
        self.phN = Entry(self.rt,width=int(self.width/23.4)) # phone number
        
        # batch year ########################
        self.yrB = StringVar()
        vlist = ["Batch 2017","Batch 2018","Batch 2019","Batch 2020"]
        self.batchCombo = ttk.Combobox(self.rt, width = int(self.width/41), textvariable = self.yrB, values=vlist)
        
        # hostel #############################
        self.Hstl = StringVar()
        self.chkBox = Checkbutton(self.rt, text='Check if you need Hostel Facility',variable=self.Hstl, onvalue=True, offvalue=False)
        self.chkBox.deselect()
        
        
        #position variables
        yOffset = self.height/19.2 #20
        interval = self.height/9.6 #40
        xoff = self.width/2826.206896552 #m0.29
        
        # placing the input widgets on the screen
        self.eyName.place(anchor=NW, relx=0.72, y = yOffset)
        self.eyRll.place(anchor=NW, relx=0.72, y = yOffset + interval)
        self.radioMl.place(anchor=NW, relx=0.72, y = yOffset + 2 * interval)
        self.radioFml.place(anchor=NE, relx=1, y = yOffset + 2 * interval)
        self.AoC.place(anchor=NW, relx=0.72, y = yOffset + 3 * interval)
        self.phN.place(anchor=NW, relx=0.72, y = yOffset + 4 * interval)
        self.batchCombo.place(anchor=NE, relx=1, y = yOffset + 5 * interval)
        self.chkBox.place(anchor=NE, relx=1, y = yOffset + 6 * interval)
        
        # placeing the lables on the screen
        for i in range(len(lblList)):
            lblList[i].place(anchor=NE, relx = xoff, y = (yOffset + (i * interval)))
    
    
    def wrtInJson(self,data,flName): # function to write data in the JSON file
        with open(flName,'w') as f:
            json.dump(data, f, indent=4)
        
        
        
    def saveFile(self): # function to fetch the data from the fileds and then saving in the JSON
        hstl = False
        if self.Hstl.get() == '1':
            hstl = True
            
        #Saving the records in Student.json
        nstds = {
            "Rollno": self.eyRll.get(),
            "Name": self.eyName.get(),
            "Gender": self.chGender.get(),
            "address": self.AoC.get(),
            "Phone no": self.phN.get(),
            "Batch": self.yrB.get(),
            "Hostel": hstl
        }        
        
        fl = ""
        try: # try to open the file if already exsists, it means we have to append the data without loosing the data already in the JSON
            fl = open(self.dataFile,"r") 
            details = json.load(fl)
            temp = details["Students"]
            temp.append(nstds)
            self.wrtInJson(details,self.dataFile)
            
        except IOError: # if no JSON found create a new aone and add data to it
            fl = open(self.dataFile,"w")
            d = {
                "Students":[nstds]}
            json.dump(d,fl,indent=4)
        fl.close()
        msgBox = messagebox.showinfo("Save","Your record has been saved") # popup nessage box to tell the user that the data has been saved
        self.clearInput()

        
        
    def clearInput(self): # clearing all the fields ####################################
        self.eyName.delete(0,'end')
        self.eyRll.delete(0,'end')
        self.AoC.delete(0,'end')
        self.phN.delete(0,'end')
        self.chGender.set(0)
        self.batchCombo.delete(0,'end')
        self.chkBox.deselect()
        
        
    # SAVE BUTTON TOOL TIP #########################################################
    def svBttnHvr(self,e):
        self.svBtnLabel.config(text="Save records",borderwidth=2,relief="ridge")
        self.svBtnLabel.place(anchor=NE,relx=0.46,y=int(self.height/1.28)+25)
    def svBttnLv(self,e):
        self.svBtnLabel.config(text="",borderwidth=0,relief="flat")    
        self.svBtnLabel.place(anchor=NE,relx=0,y=int(self.height/1.28)+25)
    # ##############################################################################
    
    
    # save and clear buttons ########################################################
    def bttns(self):
        saveBttn = Button(self.rt,text="Save",command=self.saveFile,width=15)
        self.svBtnLabel = Label(self.rt,text=None)
        saveBttn.bind('<Enter>',self.svBttnHvr)
        saveBttn.bind('<Leave>',self.svBttnLv)
        clearBttn = Button(self.rt,text="Clear",command=self.clearInput,width=15)

        clearBttn.place(anchor=NE,relx=0.65,y=int(self.height/1.28))
        saveBttn.place(anchor=NE,relx=0.47,y=int(self.height/1.28))
        
