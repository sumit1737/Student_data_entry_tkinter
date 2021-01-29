from tkinter import *
from tkinter import ttk
from NewStudent import *        # Module 1 for entering new students details
from Display import *           # Module 2 for displaying the students and their info
from CourseCreate import *      # Module 3 for creating new course
from DisplayCourse import *     # Moudle 4 for displaying the Courses
from AllocateCourse import *    # Module 5 for allocating courses to the students


class Game(): # the main root window class
   def __init__(self):
      self.root = Tk()
      self.WIDTH = self.root.winfo_screenwidth() # Width of the root window
      self.HEIGHT = self.root.winfo_screenheight() # Height of the root window
      self.createWindow() # creating the window and filling the background color
      
   def createWindow(self):
      try:
         self.root.attributes("-zoomed",True) # Fullscreen window for linux (This was programmed in linux)
      except:
         self.root.geometry("%dx%d" % (self.WIDTH, self.HEIGHT)) # Fullscreen for window OS
      self.root.configure(bg="black") # background color of the window
      self.root.title("Student Record Keeping Application") # Title of the window
      
      #height and width of the inner frame containing the notebook widget
      self.WorkH = int(2.5*(self.HEIGHT / 5 )) 
      self.WorkW = int(3*(self.WIDTH / 5 ))
      
      #setting the minimum size of the window in case of resize
      self.root.minsize((self.WorkW+int(self.WorkW/10)),self.HEIGHT-40)
   
   def makeTabView(self):
      tabW = self.WorkW
      tabH = self.WorkH
      
      # NOTE BOOK #############################################
      nBook = ttk.Notebook(self.mainFrame)
      nBook.pack(padx=10,pady=10)
      # ########################################################

      # NEW STUDENT ############################################
      new_student = Frame(nBook,width=tabW,height=tabH)
      nBook.add(new_student, text='New Student')
      nS = nStudent(new_student,self.WorkW,self.WorkH)
      nS.labels()
      nS.bttns()
      # ########################################################
      
      # DISPLAY ################################################
      display_st_info = Frame(nBook, width=tabW,height=tabH)
      nBook.add(display_st_info, text='Display')
      disp = Disp(display_st_info,self.WorkW,self.WorkH)
      disp.dispStdnt()
      # ########################################################
      
      # COURSE CREATION ########################################
      createCourse = Frame(nBook, width=tabW,height=tabH)
      nBook.add(createCourse, text='Course Creation')
      nC = nCourse(createCourse, self.WorkW, self.WorkH)
      nC.labels()
      nC.bttns()
      # ########################################################
      
      # DISPLAY COURSES ########################################
      display_crs = Frame(nBook, width=tabW,height=tabH)
      nBook.add(display_crs, text='Display Courses')
      dispCrs = DispCrs(display_crs, self.WorkW, self.WorkH)
      dispCrs.table()
      # ########################################################
      
      
      # COURSE ALLOCATION ######################################
      alloc_crs = Frame(nBook, width=tabW,height=tabH)
      nBook.add(alloc_crs, text='Course Allocation')
      allocateCrs = allocCourse(alloc_crs, self.WorkW, self.WorkH)
      allocateCrs.labels()
      allocateCrs.bttns()
      # ########################################################
      
      
   def fillRootWindow(self):
      # IMAGES ON THE MAIN WINDOW #####################################################
      self.img1 = PhotoImage(file="eLogo.gif")
      iLabel1 = Label(self.root,image=self.img1,relief="flat",width=118,height=68)
      iLabel1.place(x=10,y=10)
      
      self.img2 = PhotoImage(file="cLogo.gif")
      iLabel2 = Label(self.root,image=self.img2,relief="flat",width=178,height=74)
      iLabel2.place(relx=1,y=5,anchor=NE)
      
      self.img3 = PhotoImage(file="pLogo.gif")
      iLabel3 = Label(self.root,image=self.img3,relief="flat",width=135,height=73)
      iLabel3.place(relx=0.03,rely=0.5,anchor=W)
      # ###############################################################################
      
      # TEXT ON THE MAIN WINDOW ####################################################################
      fntStyle = tkFont.Font(size=30)
      chktUni = Label(self.root,text="Chitkara University", bg="black", fg="white",font=fntStyle)
      chktUni.place(relx=0.5,rely=0,anchor=N)
      
      fntStyle = tkFont.Font(size=30,family="Times")
      stuMgm = Label(self.root,text="STUDENT DATABASE", bg="black", fg="white",font=fntStyle)
      stuMgm.place(relx=0.5,rely=0.22,anchor=S)
      
      fntStyle = tkFont.Font(family="Arial", size=15, weight="bold")
      stuMgm = Label(self.root,text="Department of Computer Science & Engineering", bg="black", fg="white",font=fntStyle)
      stuMgm.place(relx=0.5,rely=0.92,anchor=S)
      # ##########################################################################################
      
      
      # MAKING AND PLACING THE MAIN FRAME ON THE ROOT WINDOW ####################################
      self.mainFrame = Frame(self.root, height=self.WorkH, width=self.WorkW)
      self.mainFrame.place(relx=0.5, rely=0.5,anchor=CENTER)
      # #########################################################################################
      
   
   def gameLoop(self):
      self.fillRootWindow() # filling the root window
      self.makeTabView() # making the tab view (notebook) in the main frame
      self.root.mainloop() # the even loop
      

G = Game() # object for the student database system
G.gameLoop() # running the window