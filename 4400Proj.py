from tkinter import *
#import pymysql
import os
from re import findall

class CS4400:
#Login Page done
    def __init__(self,win):
        self.loginWin = win
        self.loginWin.title("Login")
        userLab= Label(self.loginWin,text="Username:")
        userLab.grid(row=0,column=0)
        passLab= Label(self.loginWin,text="Password:")
        passLab.grid(row=1,column=0)
        self.user = StringVar()
        userEnt =Entry(self.loginWin, width =30, textvariable = self.user)
        userEnt.grid(row=0, column =1)
        self.passw = StringVar()
        passEnt =Entry(self.loginWin, width =30, textvariable = self.passw,)
        passEnt.grid(row =1, column =1)
        self.loginBut =Button(self.loginWin, text="Login", command = self.Login)
        self.loginBut.grid(row=2,column=0)
        self.regisBut =Button(self.loginWin, text="Register", command = self.Register)
        self.regisBut.grid(row=2,column=1)

    def Login(self):
        #called by _init_
        username = self.user.get()
        password =self.passw.get()
        # Need SQL Code to check if login is succesful
        # need SQL COde to check flag type of user 
        # if self.flag="Admin":
            #self.ChooseFunc()
        #else:
        # self.flag="Student"
        
        print("Logged in")
        print(username)
        print(password)
        if username == "tylerhall":  #this is temporary; would normally be a
                                        #admin username (will have to get from SQL)
            self.ChooseFunc()
        else:
            print("Invalid username") #this will need to become an error window
        #self.loginWin.destroy() # will  need to do once a login is accepted
            #this is done inside ChooseFunc function for admin users
        self.Main_page() #will need to put under else once sql is added
            #this only needs to happen if a student logs in

    def ChooseFunc(self):
        #this function is called by Login if the user logs in as a Admin

        #creates Choose Functionality window and hides Login window
        self.chooseFuncWin = Toplevel()
        self.loginWin.withdraw()
        self.chooseFuncWin.title("Choose Functionality")
        #Creating Choose Functionality labels and buttons
        chooseLab = Label(self.chooseFuncWin, text="Choose Functionality")
        chooseLab.grid(row=0,column=0)
        self.viewAppBut = Button(self.chooseFuncWin, text="View Applications",command=self.View_apps)
        self.viewAppBut.grid(row=1,column=0)
        self.viewPopProjBut = Button(self.chooseFuncWin, text="View Popular Project Report",command=self.Popular_Project)
        self.viewPopProjBut.grid(row=2,column=0)
        self.viewAppRepBut = Button(self.chooseFuncWin, text="View Application Report",command=self.App_report)
        self.viewAppRepBut.grid(row=3,column=0)
        self.addProjBut = Button(self.chooseFuncWin, text="Add a Project", command=self.Add_proj)
        self.addProjBut.grid(row=4,column=0)
        self.addCourseBut = Button(self.chooseFuncWin, text="Add a Course", command=self.Add_course)
        self.addCourseBut.grid(row=5,column=0)
        self.logOutBut = Button(self.chooseFuncWin, text="Log Out")#need to add a command here
        self.logOutBut.grid(row=6,column=0)


    def Popular_Project(self):
        #called by ChooseFunc (clicking "View Popular Proj" button on Choose Func window)

        #creates Popular Project Report window and hides Choose Functionality window
        self.popProjWin = Toplevel()
        self.chooseFuncWin.withdraw()
        #creates objects within Pop Proj window
        self.popProjWin.title("Popular Project Report")
        popProjLab = Label(self.popProjWin, text = "Popular Project")
        popProjLab.grid(row=0,column=0)
        #this will need to change, placeholder until I figure out how to insert a table
        self.Table = Label(self.popProjWin, text = "**Table will go here**")
        self.Table.grid(row=1,column=0)
        self.backBut = Button(self.popProjWin, text = "Back",command=self.Back_Popular_Project)
        self.backBut.grid(row=2,column=0)


    def Back_Popular_Project(self):
        #called by Popular_Project (by clicking back button to go back to Choose Func window)
        
        self.ChooseFunc()
        self.popProjWin.withdraw()

    def Back_View_apps(self):
        #called by View_apps (by clicking back button to go back to Choose Func window)
        
        self.ChooseFunc()
        self.viewAppsWin.withdraw()

    def Back_Add_course(self):
        #called by Add_course (by clicking back button to go back to Choose Func window)

        self.ChooseFunc()
        self.addCourseWin.withdraw()
        
        
        

    def Register(self):
        #called by _init_
        print("Registered")
        self.loginWin.withdraw()
        #creates registration window
        self.registerWin = Toplevel()
        self.registerWin.title("Register")
        #create username label
        userLab= Label(self.registerWin,text="Username:")
        userLab.grid(row=0,column=0)
        #create email label
        emailLab= Label(self.registerWin,text="GT Email Address:")
        emailLab.grid(row=1,column=0)
        #create password label
        passLab = Label(self.registerWin, text = "Password:")
        passLab.grid(row=2, column=0)
        #create confirm password label
        confLab = Label(self.registerWin, text = "Confirm Password:")
        confLab.grid(row=3, column=0)
        #create username text field
        self.user = StringVar()
        userEnt =Entry(self.registerWin, width =30, textvariable = self.user)
        userEnt.grid(row=0, column =1)
        #create email text field
        self.email = StringVar()
        emailEnt =Entry(self.registerWin, width =30, textvariable = self.email,)
        emailEnt.grid(row =1, column =1)
        #create password text field
        self.passw = StringVar()
        passEnt = Entry(self.registerWin, width=30, textvariable = self.passw,)
        passEnt.grid(row=2, column=1)
        #create confirm password text field
        self.conf = StringVar()
        confEnt = Entry(self.registerWin, width=30, textvariable = self.conf,)
        confEnt.grid(row=3, column=1)
        #Creates a create button
        #Left as redirecting to login page. Can change if needed.
        self.createBut =Button(self.registerWin, text="Create", command = self.RegisterCheck)
        self.createBut.grid(row=4,column=0)
        print("testing")
        #self.registerWin.deiconify() Moved to function below, only want to destroy windoe if register is good

    def RegisterCheck(self):
        print("Register check")
        username = self.user.get()
        userEmail = self.email.get()
        password =self.passw.get()
        confirmPass = self.conf
        print(username, userEmail, password, confirmPass)
        print("calling main page")
        self.registerWin.destroy()
        self.Main_page() #ONLY RUN IF A SUCCESFUL REGISTER
        
    def Main_page(self):
        #called by ME Page
        #also called by a succesfull login page
        self.loginWin.withdraw()
        #self.registerWin.withdraw()
        self.Main_pageWin = Toplevel()
        self.Main_pageWin.title("Main Page")
        MainPageLab1 = Label(self.Main_pageWin, text="Title:")
        MainPageLab1.grid(row=0,column=0)
       # print ("Main page Should be showing...?")
        self.MPEntry=StringVar()
        MainPageEnt=Entry(self.Main_pageWin, width=30, textvariable=self.MPEntry)
        MainPageEnt.grid(row=0, column=1)
        MainPageLab2 = Label(self.Main_pageWin, text="Category:")
        MainPageLab2.grid(row=0,column=2)
        self.MainPageCat=StringVar()
        self.MainPageCat.set("Please Select")
        #USE SQL to call list of category names called self.catlist
        self.catlist=["Add cat1 here"," Add Cat 2 here", "Cat 3", "Cat 4", "Cat 5"]
        self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat,*self.catlist)
        self.MainPagedrop.grid(row=0,column=3)
        self.MainPageRow = 0
        self.AddCatBut =Button(self.Main_pageWin, text="Add a Category", command = self.Add_Cat_MainPage)
        self.AddCatBut.grid(row=0,column=4)

        MainPageLabDes = Label(self.Main_pageWin,text="Designation:")
        MainPageLabDes.grid(row=1,column=0)
        #print("ran")
        self.MainPageDes=StringVar()
        self.MainPageDes.set("Please Select")
        #USE SQL to call list of Designation names called self.deslist
        self.deslist=["Add des1 here"," Add des2 here"]
        self.MainPageDesdrop=OptionMenu(self.Main_pageWin,self.MainPageDes,*self.deslist)
        self.MainPageDesdrop.grid(row=1,column=1)

        MainPageLabMaj = Label(self.Main_pageWin,text="Major:")
        MainPageLabMaj.grid(row=2,column=0)
        #print("ran")
        self.MainPageMaj=StringVar()
        self.MainPageMaj.set("Please Select")
        #USE SQL to call list of Designation names called self.deslist
        self.majlist=["Add maj1 here"," Add maj2 here"]
        self.MainPageMajdrop=OptionMenu(self.Main_pageWin,self.MainPageMaj,*self.majlist)
        self.MainPageMajdrop.grid(row=2,column=1)

        MainPageLabYear = Label(self.Main_pageWin,text="Year:")
        MainPageLabYear.grid(row=3,column=0)
        #print("ran")
        self.MainPageYear=StringVar()
        self.MainPageYear.set("Please Select")
        #USE SQL to call list of Designation names called self.deslist
        self.yearlist=["Freshman","Sophmore","Junior","Senior"]
        self.MainPageYeardrop=OptionMenu(self.Main_pageWin,self.MainPageYear,*self.yearlist)
        self.MainPageYeardrop.grid(row=3,column=1)

        self.CatTempList=[]

        #Radio BUttons
        self.MainPageRB=StringVar()
        self.ProjButtonMP= Radiobutton(self.Main_pageWin, text="Project", value="Project", variable=self.MainPageRB)
        self.ProjButtonMP.grid(row=3,column=2)
        self.CourseButtonMP= Radiobutton(self.Main_pageWin, text="Course", value="Course", variable=self.MainPageRB)
        self.CourseButtonMP.grid(row=3,column=3)
        self.BothButtonMP= Radiobutton(self.Main_pageWin, text="Both", value="Both", variable=self.MainPageRB)
        self.BothButtonMP.grid(row=3,column=4)

        self.FilterBut =Button(self.Main_pageWin, text="Apply Filter", command = self.Apply_Filter)
        self.FilterBut.grid(row=4,column=3)
        self.ResetBut =Button(self.Main_pageWin, text="Reset Filter", command = self.Reset_Filter)
        self.ResetBut.grid(row=4,column=4)
        
#Course Project List# may need to add scroll bar??

        self.CPframe=Frame(self.Main_pageWin,bd= 3,bg="black")
        self.CPframe.grid(row=5, column=0,columnspan= 5)
        MPCPlab1= Label(self.CPframe, text ="Name", width=70,bg="Light Blue")
        MPCPlab1.grid(row=0,column=0,sticky=W,padx=3,pady=1)
        MPCPlab2= Label(self.CPframe, text ="Type",width=20,bg="Light Blue")
        MPCPlab2.grid(row=0,column=1,sticky=W,pady=1)
        #pull al list of all courses anf projects here will need SQL
        CPframeCounter=1
        self.CPlist =[("Project A","Project"),("Project B","Project"),("Course A", "Course"),("COurse B","Course"),("Prject Q","Project")]
        for tup in self.CPlist:
            Name=tup[0]
            typ=tup[1]
            lab=Label(self.CPframe, text =str(Name), width=70)
            lab.grid(row=CPframeCounter,column=0,sticky=W,padx=3,pady=1)
            lab=Label(self.CPframe, text =str(typ), width=20)
            lab.grid(row=CPframeCounter,column=1,sticky=W,pady=1)
            CPframeCounter=CPframeCounter+1


    def Apply_Filter(self):
        print("apply filter")
        
    def Reset_Filter(self):
        print("Reset Filter")
        self.Main_pageWin.destroy()
        self.Main_page()
        
    def Add_Cat_MainPage(self):
        if self.MainPageCat.get() == "Please Select" :
            return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")
        
        self.MainPageRow = self.MainPageRow +1

        
        if self.MainPageRow == 1:
            self.CatTempList.append(self.MainPageCat.get())
          
        
        if self.MainPageRow > 1: 
            if self.MainPageCat1.get() == "Please Select":
                self.MainPageRow = self.MainPageRow - 1
                return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")
            
            if self.MainPageCat1.get() not in self.CatTempList:
                self.CatTempList.append(self.MainPageCat1.get())

            else:
                self.MainPageRow = self.MainPageRow - 1
                return messagebox.showerror("OOps!","Please Do not Repeat Categories")
        
        if self.MainPageRow >= len(self.catlist): #-1:
          self.AddCatBut.config(state="disabled")
          return messagebox.showerror("OOps!","You have reached the maximum amount of Categories that can be added")
            
        
        self.Main_pageWin.destroy()
 
        
        self.Main_pageWin = Toplevel()
        self.Main_pageWin.title("Main Page")
        MainPageLab1New = Label(self.Main_pageWin, text="Title:")
        MainPageLab1New.grid(row=0,column=0)

      
        self.MPEntry.set(self.MPEntry.get())
        MainPageEnt=Entry(self.Main_pageWin, width=30, textvariable=self.MPEntry)
        MainPageEnt.grid(row=0, column=1)
        MainPageLab2 = Label(self.Main_pageWin, text="Category:")
        MainPageLab2.grid(row=0,column=2)
        
      
        self.MainPageCat.set(self.MainPageCat.get())
        self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat,*self.catlist)
        self.MainPagedrop.grid(row=0,column=3)
        self.MainPagedrop.config(state="disabled")
 
     
        MainPageLabDes = Label(self.Main_pageWin,text="Designation:")
        MainPageLabDes.grid(row=1,column=0)
        self.MainPageYear.set(self.MainPageYear.get())
        self.MainPageDesdrop=OptionMenu(self.Main_pageWin,self.MainPageDes,*self.deslist)
        self.MainPageDesdrop.grid(row=1,column=1)

        MainPageLabMaj = Label(self.Main_pageWin,text="Major:")
        MainPageLabMaj.grid(row=2,column=0)
        self.MainPageMaj.set(self.MainPageMaj.get())
        self.MainPageMajdrop=OptionMenu(self.Main_pageWin,self.MainPageMaj,*self.majlist)
        self.MainPageMajdrop.grid(row=2,column=1)

        MainPageLabYear = Label(self.Main_pageWin,text="Year:")
        MainPageLabYear.grid(row=3,column=0)
        self.MainPageYear.set(self.MainPageYear.get())
        self.MainPageYeardrop=OptionMenu(self.Main_pageWin,self.MainPageYear,*self.yearlist)
        self.MainPageYeardrop.grid(row=3,column=1)
 
        for item in range(1,self.MainPageRow+1):
            
            if item == self.MainPageRow:
                
                self.MainPageCat1=StringVar()
                self.MainPageCat1.set("Please Select")
                self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat1,*self.catlist)
                self.MainPagedrop.grid(row=item,column=3)
            else:
                self.MainPageCat1=StringVar()
                self.MainPageCat1.set(self.CatTempList[item])
                self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat1,*self.catlist)
                self.MainPagedrop.grid(row=item,column=3)
                self.MainPagedrop.config(state="disabled")
        
        self.AddCatBut =Button(self.Main_pageWin, text="Add a Category", command = self.Add_Cat_MainPage)
        self.AddCatBut.grid(row=self.MainPageRow,column=4)

        self.MainPageRB.set(self.MainPageRB.get())
        self.ProjButtonMP= Radiobutton(self.Main_pageWin, text="Project", value="Project", variable=self.MainPageRB)
        self.ProjButtonMP.grid(row=self.MainPageRow+1,column=2)
        self.CourseButtonMP= Radiobutton(self.Main_pageWin, text="Course", value="Course", variable=self.MainPageRB)
        self.CourseButtonMP.grid(row=self.MainPageRow+1,column=3)
        self.BothButtonMP= Radiobutton(self.Main_pageWin, text="Both", value="Both", variable=self.MainPageRB)
        self.BothButtonMP.grid(row=self.MainPageRow+1,column=4)

        self.FilterBut =Button(self.Main_pageWin, text="Apply Filter", command = self.Apply_Filter)
        self.FilterBut.grid(row=self.MainPageRow+2,column=3)
        self.ResetBut =Button(self.Main_pageWin, text="Reset Filter", command = self.Reset_Filter)
        self.ResetBut.grid(row=self.MainPageRow+2,column=4)
        
         #Course Project List
        self.CPframe=Frame(self.Main_pageWin,bd= 3,bg="black")
        self.CPframe.grid(row=self.MainPageRow+3, column=0,columnspan= 5)
        MPCPlab1= Label(self.CPframe, text ="Name", width=70,bg="Light Blue")
        MPCPlab1.grid(row=0,column=0,sticky=W,padx=3,pady=1)
        MPCPlab2= Label(self.CPframe, text ="Type",width=20,bg="Light Blue")
        MPCPlab2.grid(row=0,column=1,sticky=W,pady=1)
        #pull al list of all courses anf projects here will need SQL
        CPframeCounter=1
        # list should be defined as all or as apply filter?
 #       self.CPlist =[("Project A","Project"),("Project B","Project"),("Course A", "Course"),("COurse B","Course"),("Prject Q","Project")]
        for tup in self.CPlist:
            Name=tup[0]
            typ=tup[1]
            lab=Label(self.CPframe, text =str(Name), width=70)
            lab.grid(row=CPframeCounter,column=0,sticky=W,padx=3,pady=1)
            lab=Label(self.CPframe, text =str(typ), width=20)
            lab.grid(row=CPframeCounter,column=1,sticky=W,pady=1)
            CPframeCounter=CPframeCounter+1

    def Me_page(self):
        #called by
        #Creates ME window
        #destroy previous window
        self.meWin = win
        self.meWin.title("ME")
        self.profBut = Button(self.meWin, text = "Edit Profile", command = self.Edit_profile)
        self.profBut.grid(row=0, column=0)
        self.applBut = Button(self.meWin, text = "My Applications", command = self.My_app)
        self.applBut.grid(row=1, column=0)
        self.backBut = Button(self.meWin, text = "Back", command = self.Main_page)
        self.backBut.grid(row=2, column=0)
        self.meWin.deiconify()

    def Edit_profile(self):
        #called by Me Page
        print ("edit profile")

    def My_app(self):
        #called my Me Page
        print ("my apps")

    def View_proj(self):
        #called by
        print ("view project page")

    def View_course(self):
        #called by
        print ("view course page")


    def View_apps(self):
        #called by the "View applications button" in the Choose Functionality Pgae

        #self.chooseFunWin.withdraw()

        #creates View Apps window
        self.viewAppsWin = Toplevel()
        self.chooseFuncWin.withdraw()
        self.viewAppsWin.title("Application")

        #frame to put the Apllications in
        projectFrame = Frame(self.viewAppsWin)
        projectFrame.grid(row = 0, column = 0, columnspan = 6)

        #Labels for Project, Applicant Major/Year, Status
        projectLabel =Label(projectFrame, text="Project",width = 20)
        projectLabel.grid(row = 0, column=0,padx = 5, pady=5 )

        appMajorLabel =Label(projectFrame, text="Applicant Major",width = 20)
        appMajorLabel.grid(row = 0, column=1,padx = 5, pady=5 )

        appYearLabel =Label(projectFrame, text="Applicant Year",width = 20)
        appYearLabel.grid(row = 0, column=2,padx = 5, pady=5 )

        statusLabel =Label(projectFrame, text="Status",width = 20)
        statusLabel.grid(row = 0, column=3,padx = 5, pady=5 )
        
        #creates frame for Back Accept Reject Button
        buttonFrame = Frame(self.viewAppsWin)
        buttonFrame.grid(row = 1, column = 0, columnspan = 6)

        backButton = Button(buttonFrame, text = "Back",width = 15, command = self.Back_View_apps)
        backButton.grid(row = 0,column = 0 ,  sticky = E)
        acceptButton = Button(buttonFrame, text = "Accept",width = 15)#, command =self.acceptApplicant)
        acceptButton.grid(row = 0,column = 3,  sticky = E)
        rejectButton = Button(buttonFrame, text = "Reject",width = 15)#, command =self.rejectApplicant)
        rejectButton.grid(row = 0,column = 4,  sticky = E)

        #We have to import all Project/Applicant names/year / Status from Database
        #Create function for radiobuttons that will only be assgned to the Project that have status: Pending


    def App_report(self):
        #called by
        print("admin view application reports")

    def Add_proj(self):
        #called by

        self.addProjectWin = Toplevel()
        self.chooseFuncWin.withdraw()
        self.addProjectWin.title("Add a Project")
        print("admin add project")
        
    def Add_course(self):
        #called by Button "add course" in the choose functionality function

        #self.chooseFunWin.withdraw()

        #creates Add Course window and hides Choose Func window
        self.addCourseWin = Toplevel()
        self.chooseFuncWin.withdraw()
        self.addCourseWin.title("Add a Course")

        #frame to put the Course#/Course Name/Instructor/Designation/Ctaegory/Est Students in 
        courseInfoFrame = Frame(self.addCourseWin)
        courseInfoFrame.grid(row = 0, column = 0, columnspan = 6)

        #LABELS
        courseNumLab = Label(courseInfoFrame, text="Course Number:")
        courseNumLab.grid(row =0, column = 0) 

        courseNameLab = Label(courseInfoFrame, text="Course Name:")
        courseNameLab.grid(row =1, column = 0)

        instructorLab = Label(courseInfoFrame, text="Instructor:")
        instructorLab.grid(row =2, column = 0)

        designationLab = Label(courseInfoFrame, text="Designation:")
        designationLab.grid(row =3, column = 0)

        categoryLab = Label(courseInfoFrame, text="Category:")
        categoryLab.grid(row =4, column = 0)

        estimatedNumStudentsLab = Label(courseInfoFrame, text="Estimated # of students:")
        estimatedNumStudentsLab.grid(row =5, column = 0) 
        

        #Entries for labels

        self.newCourseNum = StringVar()
        courseNumEnt =Entry(courseInfoFrame, width =30, textvariable = self.newCourseNum)
        courseNumEnt.grid(row=0, column =1)

        self.newCourseName = StringVar()
        courseNameEnt =Entry(courseInfoFrame, width =30, textvariable = self.newCourseName)
        courseNameEnt.grid(row=1, column =1)

        self.newInstructor = StringVar()
        newInstructorEnt =Entry(courseInfoFrame, width =30, textvariable = self.newInstructor)
        newInstructorEnt.grid(row=2, column =1)

        self.estNumStudents = StringVar()
        estNumStudentsEnt =Entry(courseInfoFrame, width =30, textvariable = self.estNumStudents)
        estNumStudentsEnt.grid(row=5, column =1)

        self.addCourseDes=StringVar()
        self.addCourseDes.set("Please Select")
        #USE SQL to call list of Designation names called self.deslist
        self.deslist=["Add des1 here"," Add des2 here"]
        self.addCourseDesdrop=OptionMenu(courseInfoFrame,self.MainPageDes,*self.deslist)
        self.addCourseDesdrop.grid(row=3,column=1)

        #Put Buttons in Frame
        buttonFrame = Frame(self.addCourseWin)
        buttonFrame.grid(row = 1, column = 0, columnspan = 6)

        backButton = Button(buttonFrame, text = "Back",width = 15, command = self.Back_Add_course)
        backButton.grid(row = 0,column = 0 ,  sticky = E)
        
        submitButton = Button(buttonFrame, text = "Accept",width = 15)#, command =self.submitNewCourse)
        submitButton.grid(row = 0,column = 1,  sticky = E)
    

win = Tk()
app = CS4400(win)
win.mainloop()
