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

        self.backBut = Button(self.popProjWin, text = "Back",command=self.Back_Popular_Project)
        self.backBut.grid(row=2,column=0)

        #frame for table
        self.popProjectFrame = Frame(self.popProjWin,bd= 3,bg="black")
        self.popProjectFrame.grid(row = 1, column = 0, columnspan = 6)

        #Labels for Project, # of Applicants 
        projectLabel =Label(self.popProjectFrame, text="Project",width = 20,bg="Light Blue")
        projectLabel.grid(row = 0, column=0,sticky=W,padx=3,pady=1)

        numApplicantsLabel =Label(self.popProjectFrame, text="Number of Applicants",width = 20,bg="Light Blue")
        numApplicantsLabel.grid(row = 0, column=1,sticky=W,padx=3,pady=1)

        #pull most pop project and # of applicants using SQL
        popProjectframeCounter=1
        self.projMajYearStatlist =[("Project A","34"),("Project B","55"),("Project C","67"),("Project F","69")]
        for tup in self.projMajYearStatlist:
            projectName=tup[0]
            numApplicants=tup[1]
            
            lab=Label(self.popProjectFrame, text =str(projectName), width=20)
            lab.grid(row=popProjectframeCounter,column=0,sticky=W,padx=3,pady=1)
            
            lab=Label(self.popProjectFrame, text =str(numApplicants), width=20)
            lab.grid(row=popProjectframeCounter,column=1,sticky=W,padx=3,pady=1)
            
            popProjectframeCounter=popProjectframeCounter+1


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
        
    def Back_App_report(self):

        self.ChooseFunc()
        self.applicationReportWin.withdraw()

    def Back_View_Project(self):
        #called by View_Project (by clicking back button to go back to Main menu window)

        self.Main_page()
        self.viewProjWin.withdraw()
        

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
        self.mepagebut=Button(self.Main_pageWin, text="ME PAGE", command = self.Me_page)
        self.mepagebut.grid(row=0,column=0)
        MainPageLab1 = Label(self.Main_pageWin, text="Title:")
        MainPageLab1.grid(row=1,column=0)
       # print ("Main page Should be showing...?")
        self.MPEntry=StringVar()
        MainPageEnt=Entry(self.Main_pageWin, width=30, textvariable=self.MPEntry)
        MainPageEnt.grid(row=1, column=1)
        MainPageLab2 = Label(self.Main_pageWin, text="Category:")
        MainPageLab2.grid(row=1,column=2)
        self.MainPageCat=StringVar()
        self.MainPageCat.set("Please Select")
        #USE SQL to call list of category names called self.catlist
        self.catlist=["Add cat1 here"," Add Cat 2 here", "Cat 3", "Cat 4", "Cat 5"]
        self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat,*self.catlist)
        self.MainPagedrop.grid(row=1,column=3)
        self.MainPageRow = 0
        self.AddCatBut =Button(self.Main_pageWin, text="Add a Category", command = self.Add_Cat_MainPage)
        self.AddCatBut.grid(row=1,column=4)

        MainPageLabDes = Label(self.Main_pageWin,text="Designation:")
        MainPageLabDes.grid(row=2,column=0)
        #print("ran")
        self.MainPageDes=StringVar()
        self.MainPageDes.set("Please Select")
        #USE SQL to call list of Designation names called self.deslist
        self.deslist=["Add des1 here"," Add des2 here"]
        self.MainPageDesdrop=OptionMenu(self.Main_pageWin,self.MainPageDes,*self.deslist)
        self.MainPageDesdrop.grid(row=2,column=1)

        MainPageLabMaj = Label(self.Main_pageWin,text="Major:")
        MainPageLabMaj.grid(row=3,column=0)
        #print("ran")
        self.MainPageMaj=StringVar()
        self.MainPageMaj.set("Please Select")
        #USE SQL to call list of Designation names called self.deslist
        self.majlist=["Add maj1 here"," Add maj2 here"]
        self.MainPageMajdrop=OptionMenu(self.Main_pageWin,self.MainPageMaj,*self.majlist)
        self.MainPageMajdrop.grid(row=3,column=1)

        MainPageLabYear = Label(self.Main_pageWin,text="Year:")
        MainPageLabYear.grid(row=4,column=0)
        #print("ran")
        self.MainPageYear=StringVar()
        self.MainPageYear.set("Please Select")
        #USE SQL to call list of Designation names called self.deslist
        self.yearlist=["Freshman","Sophmore","Junior","Senior"]
        self.MainPageYeardrop=OptionMenu(self.Main_pageWin,self.MainPageYear,*self.yearlist)
        self.MainPageYeardrop.grid(row=4,column=1)

        self.CatTempList=[]

        #Radio BUttons
        self.MainPageRB=StringVar()
        self.ProjButtonMP= Radiobutton(self.Main_pageWin, text="Project", value="Project", variable=self.MainPageRB)
        self.ProjButtonMP.grid(row=4,column=2)
        self.CourseButtonMP= Radiobutton(self.Main_pageWin, text="Course", value="Course", variable=self.MainPageRB)
        self.CourseButtonMP.grid(row=4,column=3)
        self.BothButtonMP= Radiobutton(self.Main_pageWin, text="Both", value="Both", variable=self.MainPageRB)
        self.BothButtonMP.grid(row=4,column=4)

        self.FilterBut =Button(self.Main_pageWin, text="Apply Filter", command = self.Apply_Filter)
        self.FilterBut.grid(row=5,column=3)
        self.ResetBut =Button(self.Main_pageWin, text="Reset Filter", command = self.Reset_Filter)
        self.ResetBut.grid(row=5,column=4)

        #Course Project List
        self.CPframe=Frame(self.Main_pageWin,bd= 3,bg="black")
        self.CPframe.grid(row=6, column=0,columnspan= 5)
        MPCPlab1= Label(self.CPframe, text ="Name", width=70,bg="Light Blue")
        MPCPlab1.grid(row=0,column=0,sticky=W,padx=3,pady=1)
        MPCPlab2= Label(self.CPframe, text ="Type",width=20,bg="Light Blue")
        MPCPlab2.grid(row=0,column=1,sticky=W,pady=1)
        
        #pull al list of all courses anf projects here will need SQL
        CPframeCounter=1
        self.CPlist =[("Project A","Project"),("Project B","Project"),("Course A", "Course"),("COurse B","Course"),("Prject Q","ProjectQ")]
        for tup in self.CPlist:
            Name=tup[0]
            typ=tup[1]
            self.SelectBut=Button(self.CPframe, text =str(Name), width=70 ,command = self.view)
            self.SelectBut.grid(row=CPframeCounter,column=0,sticky=W,padx=3,pady=1)
            self.lab=Label(self.CPframe, text =str(typ), width=20)
            self.lab.grid(row=CPframeCounter,column=1,sticky=W,pady=1)
            CPframeCounter=CPframeCounter+1


    def View_Project(self):
        #called by Main_page (by selecting a project)

        #creating the View Project window and hiding the Main Page window
        self.viewProjWin = Toplevel()
        self.Main_pageWin.withdraw()
        self.viewProjWin.title("View Project")
        
        #creating lefthand side labels (NO SQL) and buttons within View Project window
        advisorLab = Label(self.viewProjWin, text="Advisor:")
        advisorLab.grid(row=1,column=0)
        descriptionLab = Label(self.viewProjWin, text="Description:")
        descriptionLab.grid(row=2,column=0)
        designationLab = Label(self.viewProjWin, text="Designation:")
        designationLab.grid(row=3,column=0)
        categoryLab = Label(self.viewProjWin, text="Category:")
        categoryLab.grid(row=4,column=0)
        requireLab = Label(self.viewProjWin, text="Requirements:")
        requireLab.grid(row=5,column=0)
        numStudLab = Label(self.viewProjWin, text="Estimated # of Students:")
        numStudLab.grid(row=6,column=0)
        self.backBut= Button(self.viewProjWin, text="Back",command=self.Back_View_Project)
        self.backBut.grid(row=7,column=0)
        self.applyBut = Button(self.viewProjWin, text="Apply")
        self.applyBut.grid(row=7,column=1)

        #creating title and righthand side labels (SQL INCLUDED/NEEDED)
        #need to insert SQL statements to retrieve actual information
        self.SQLprojNameLab = Label(self.viewProjWin,text="Insert Proj Name SQL")
        self.SQLprojNameLab.grid(row=0,column=0,columnspan=2)
        self.SQLadvisor = Label(self.viewProjWin, text="Insert Advisor SQL")
        self.SQLadvisor.grid(row=1,column=1)
        self.SQLdescription = Label(self.viewProjWin, text="Insert Description SQL")
        self.SQLdescription.grid(row=2,column=1)
        self.SQLdesignation = Label(self.viewProjWin, text="Insert Designation SQL")
        self.SQLdesignation.grid(row=3,column=1)
        self.SQLcategory = Label(self.viewProjWin, text="Insert Category SQL")
        self.SQLcategory.grid(row=4,column=1)
        self.SQLrequire = Label(self.viewProjWin, text="Insert Requirements SQL")
        self.SQLrequire.grid(row=5,column=1)
        self.SQLnumStud = Label(self.viewProjWin, text="Insert Estimated # of Students SQL")
        self.SQLnumStud.grid(row=6,column=1)



    def Apply_Filter(self):
        print("apply filter")
        # if  row number == to 0 (or initial valu) will need to get the value of categor
        # if row number greater than zero but les than the maximum number of categories will need to get the last selected category
        #and add it to the final list of categories being looked at 
        
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

        self.mepagebut=Button(self.Main_pageWin, text="ME PAGE", command = self.Me_page)
        self.mepagebut.grid(row=0,column=0)
        
        MainPageLab1New = Label(self.Main_pageWin, text="Title:")
        MainPageLab1New.grid(row=1,column=0)

      
        self.MPEntry.set(self.MPEntry.get())
        MainPageEnt=Entry(self.Main_pageWin, width=30, textvariable=self.MPEntry)
        MainPageEnt.grid(row=1, column=1)
        MainPageLab2 = Label(self.Main_pageWin, text="Category:")
        MainPageLab2.grid(row=1,column=2)
        
      
        self.MainPageCat.set(self.MainPageCat.get())
        self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat,*self.catlist)
        self.MainPagedrop.grid(row=1,column=3)
        self.MainPagedrop.config(state="disabled")
 
     
        MainPageLabDes = Label(self.Main_pageWin,text="Designation:")
        MainPageLabDes.grid(row=2,column=0)
        self.MainPageYear.set(self.MainPageYear.get())
        self.MainPageDesdrop=OptionMenu(self.Main_pageWin,self.MainPageDes,*self.deslist)
        self.MainPageDesdrop.grid(row=2,column=1)

        MainPageLabMaj = Label(self.Main_pageWin,text="Major:")
        MainPageLabMaj.grid(row=3,column=0)
        self.MainPageMaj.set(self.MainPageMaj.get())
        self.MainPageMajdrop=OptionMenu(self.Main_pageWin,self.MainPageMaj,*self.majlist)
        self.MainPageMajdrop.grid(row=3,column=1)

        MainPageLabYear = Label(self.Main_pageWin,text="Year:")
        MainPageLabYear.grid(row=4,column=0)
        self.MainPageYear.set(self.MainPageYear.get())
        self.MainPageYeardrop=OptionMenu(self.Main_pageWin,self.MainPageYear,*self.yearlist)
        self.MainPageYeardrop.grid(row=4,column=1)
 
        for item in range(1,self.MainPageRow+1):
            
            if item == self.MainPageRow:
                #if item ==1:
#                    item==2
                self.MainPageCat1=StringVar()
                self.MainPageCat1.set("Please Select")
                self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat1,*self.catlist)
                self.MainPagedrop.grid(row=item+1,column=3)
            else:
                self.MainPageCat1=StringVar()
                self.MainPageCat1.set(self.CatTempList[item])
                self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat1,*self.catlist)
                self.MainPagedrop.grid(row=item+1,column=3)
                self.MainPagedrop.config(state="disabled")
        
        self.AddCatBut =Button(self.Main_pageWin, text="Add a Category", command = self.Add_Cat_MainPage)
        self.AddCatBut.grid(row=self.MainPageRow+1,column=4)

        self.MainPageRB.set(self.MainPageRB.get())
        self.ProjButtonMP= Radiobutton(self.Main_pageWin, text="Project", value="Project", variable=self.MainPageRB)
        self.ProjButtonMP.grid(row=self.MainPageRow+2,column=2)
        self.CourseButtonMP= Radiobutton(self.Main_pageWin, text="Course", value="Course", variable=self.MainPageRB)
        self.CourseButtonMP.grid(row=self.MainPageRow+2,column=3)
        self.BothButtonMP= Radiobutton(self.Main_pageWin, text="Both", value="Both", variable=self.MainPageRB)
        self.BothButtonMP.grid(row=self.MainPageRow+2,column=4)

        self.FilterBut =Button(self.Main_pageWin, text="Apply Filter", command = self.Apply_Filter)
        self.FilterBut.grid(row=self.MainPageRow+3,column=3)
        self.ResetBut =Button(self.Main_pageWin, text="Reset Filter", command = self.Reset_Filter)
        self.ResetBut.grid(row=self.MainPageRow+3,column=4)

         #Course Project List
        self.CPframe=Frame(self.Main_pageWin,bd= 3,bg="black")
        self.CPframe.grid(row=self.MainPageRow+4, column=0,columnspan= 5)
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
            
            self.SelectBut=Button(self.CPframe, text =str(Name), width=70, command = self.view)
            self.SelectBut.grid(row=CPframeCounter,column=0,sticky=W,padx=3,pady=1)
            self.lab=Label(self.CPframe, text =str(typ), width=20)
            self.lab.grid(row=CPframeCounter,column=1,sticky=W,pady=1)
            CPframeCounter=CPframeCounter+1

    def view(self):
        print("View")
        print(self.lab["text"]) # only prints the last assignment of the variable not the one selected
        print(self.SelectBut["text"])
        
        
 #       will need to check if selected button is a course or a project and then run the respective view course or view project button below

    def Me_page(self):
        #called by
        #Creates ME window
        #destroy previous window
        self.Main_pageWin.withdraw()
        #print("me page running")
        self.meWin = Toplevel()
        self.meWin.title("ME")
        self.profBut = Button(self.meWin, text = "Edit Profile", command = self.Edit_profile)
        self.profBut.grid(row=0, column=0)
        self.applBut = Button(self.meWin, text = "My Applications", command = self.My_app)
        self.applBut.grid(row=1, column=0)
        self.backBut = Button(self.meWin, text = "Back", command = self.MeBack)
        self.backBut.grid(row=2, column=0)
        self.meWin.deiconify()

    def MeBack(self):
        self.meWin.withdraw()
        self.Main_page()

    def Edit_profile(self):
        #called by Me Page
        self.meWin.withdraw()
        self.editWin = Toplevel()
        self.editWin.title("Edit Profile")
        majorLab= Label(self.editWin,text="Major:")
        majorLab.grid(row=0,column=0)
        yearLab= Label(self.editWin,text="Year:")
        yearLab.grid(row=1,column=0)
        deptLab= Label(self.editWin,text="Department:")
        deptLab.grid(row=2,column=0)

        self.EditPageMaj=StringVar()
        self.EditPageMaj.set("Please Select")
        #USE SQL to call list of major names called self.majlist
        self.majlist=["Add maj1 here"," Add maj2 here"]
        self.EditPageMajdrop=OptionMenu(self.editWin,self.EditPageMaj,*self.majlist)
        self.EditPageMajdrop.grid(row=0,column=1)

        self.EditPageYr=StringVar()
        self.EditPageYr.set("Please Select")
        self.yrlist=["Freshman","Sophomore","Junior","Senior"]
        self.EditPageYrdrop=OptionMenu(self.editWin,self.EditPageYr,*self.yrlist)
        self.EditPageYrdrop.grid(row=1,column=1)

        #USE SQL to fill in the department based on the major

        #Back button and submit data
        self.backBut = Button(self.editWin, text = "Back", command = self.EditBack)
        self.backBut.grid(row=3, column=0)
        self.editWin.deiconify()
        
    def EditBack(self):
        self.editWin.withdraw()
        self.Me_page()
        

    def My_app(self):
        #called my Me Page
        #print ("my apps")
        self.meWin.withdraw()
        self.MyAppsWin = Toplevel()
        self.MyAppsWin.title("My Applications")
        f=Frame(self.MyAppsWin, bg="black")
        f.grid(row=0,column=0)
        MyALab1 =Label(f, text="Date",width = 15, bg="Light Blue")
        MyALab1.grid(row = 0, column=0,padx = 5, pady=5 )
        MyALab2 =Label(f, text="Project Name",width = 50, bg= "Light Blue")
        MyALab2.grid(row = 0, column=1,padx = 5, pady=5 )
        MyALab3 =Label(f, text="Status",width = 20, bg= "Light Blue")
        MyALab3.grid(row = 0, column=2,padx = 5, pady=5)
        self.MyAppList=[("10/11/12","Project A","Pending"),("1/11/16","Project 9","Accepted"),("12/12/95","Project 9","Rejected")]
        MyAppCounter= 1
        for tup in self.MyAppList:
            date= tup[0]
            name=tup[1]
            status=tup[2]
            MyALab1 =Label(f, text=date,width = 15)
            MyALab1.grid(row = MyAppCounter, column=0,padx = 5, pady=5 )
            MyALab2 =Label(f, text=name,width = 50)
            MyALab2.grid(row = MyAppCounter, column=1,padx = 5, pady=5 )
            MyALab3 =Label(f, text=status,width = 20)
            MyALab3.grid(row = MyAppCounter, column=2,padx = 5, pady=5)
            MyAppCounter= MyAppCounter+1
            
        MyAppBackBut=Button(self.MyAppsWin, text="Back", command=self.MyAppBack)
        MyAppBackBut.grid(row=1,column= 0)

    def MyAppBack(self):
        self.MyAppsWin.withdraw()
        self.Me_page()
        

    def View_proj(self):
        #called by
        print ("view project page")

    def View_course(self):
        #called by some function that has not been created yet? has no call right now
        #needs to be withdraw by previous pages
       # print ("view course page")
        self.ViewCourseWin=Toplevel()
        self.ViewCourseWin.title("View Course")
        #will be called from selections based on sql and main page
        self.courseListinfo=("Example Course Name","Example Instructor","Example Designation", "Example Cat", "##")
        
        VCLab1 =Label(self.ViewCourseWin, text="Course Name:",bg="Light Blue")
        VCLab1.grid(row = 0, column=0,padx = 5, pady=5 )
        VCName =Label(self.ViewCourseWin, text=self.courseListinfo[0])
        VCName.grid(row = 0, column=1,padx = 5, pady=5)
        
        VCLab1 =Label(self.ViewCourseWin, text="Instructor:",bg="Light Blue")
        VCLab1.grid(row = 1, column=0,padx = 5, pady=5 )
        VCInst =Label(self.ViewCourseWin, text=self.courseListinfo[1])
        VCInst.grid(row = 1, column=1,padx = 5, pady=5 )
        
        VCLab2 =Label(self.ViewCourseWin, text="Designation:",bg="Light Blue")
        VCLab2.grid(row = 2, column=0,padx = 5, pady=5 )
        VCDes =Label(self.ViewCourseWin, text=self.courseListinfo[2])
        VCDes.grid(row = 2, column=1,padx = 5, pady=5 )

        VCLab3 =Label(self.ViewCourseWin, text="Category",bg="Light Blue")
        VCLab3.grid(row = 3, column=0,padx = 5, pady=5 )
        VCCat =Label(self.ViewCourseWin, text=self.courseListinfo[3])
        VCCat.grid(row = 3, column=1,padx = 5, pady=5 )

        VCLab4 =Label(self.ViewCourseWin, text="Estimatied Number of Students",bg="Light Blue")
        VCLab4.grid(row = 4, column=0,padx = 5, pady=5 )
        VCNum =Label(self.ViewCourseWin, text=self.courseListinfo[4])
        VCNum.grid(row = 4, column=1,padx = 5, pady=5 )

        VCBackBut=Button(self.ViewCourseWin, text="Back", command=self.VCBack)
        VCBackBut.grid(row=5, column=0)

    def VCBack(self):
        self.ViewCourseWin.withdraw()
        self.Main_page()
        

    def View_apps(self):
        #called by the "View applications button" in the Choose Functionality Pgae

        #self.chooseFunWin.withdraw()

        #creates View Apps window
        self.viewAppsWin = Toplevel()
        self.chooseFuncWin.withdraw()
        self.viewAppsWin.title("Application")

        #frame to put the Apllications in
        self.projectFrame = Frame(self.viewAppsWin,bd= 3,bg="black")
        self.projectFrame.grid(row = 0, column = 0, columnspan = 6)

        #Labels for Project, Applicant Major/Year, Status
        projectLabel =Label(self.projectFrame, text="Project",width = 20,bg="Light Blue")
        projectLabel.grid(row = 0, column=0,sticky=W,padx=3,pady=1)

        appMajorLabel =Label(self.projectFrame, text="Applicant Major",width = 20,bg="Light Blue")
        appMajorLabel.grid(row = 0, column=1,sticky=W,padx=3,pady=1)

        appYearLabel =Label(self.projectFrame, text="Applicant Year",width = 20,bg="Light Blue")
        appYearLabel.grid(row = 0, column=2,sticky=W,padx=3,pady=1)

        statusLabel =Label(self.projectFrame, text="Status",width = 20,bg="Light Blue")
        statusLabel.grid(row = 0, column=3,sticky=W,padx=3,pady=1)

        #pull al list of all Project, Applicant Major/Year, Status
        projectframeCounter=1
        self.projMajYearStatlist =[("Project A","CS","Freshman","Pending"),("Project B","ECE","Junior","Rejected"),("Project C","IE","Senior","Pending"),("Project F","INTA","Senior","Accepted")]
        for tup in self.projMajYearStatlist:
            projectName=tup[0]
            applicantMajor=tup[1]
            applicantYear=tup[2]
            applicantStatus=tup[3]
            lab=Label(self.projectFrame, text =str(projectName), width=20)
            lab.grid(row=projectframeCounter,column=0,sticky=W,padx=3,pady=1)
            lab=Label(self.projectFrame, text =str(applicantMajor), width=20)
            lab.grid(row=projectframeCounter,column=1,sticky=W,padx=3,pady=1)
            lab=Label(self.projectFrame, text =str(applicantYear), width=20)
            lab.grid(row=projectframeCounter,column=2,sticky=W,padx=3,pady=1)
            lab=Label(self.projectFrame, text =str(applicantStatus), width=20)
            lab.grid(row=projectframeCounter,column=3,sticky=W,padx=3,pady=1)
            projectframeCounter=projectframeCounter+1

        #We have to import all Project/Applicant names/year / Status from Database
        #Create function for radiobuttons that will only be assgned to the Project that have status: Pending

        #Radio BUttons
 #       self.viewApps=StringVar()
 #       self.ProjRButton= Radiobutton(self.projectFrame, variable=self.viewApps)
 #       self.ProjRButton.grid(row=variable,column=0)

        
        #creates frame for Back Accept Reject Button
        buttonFrame = Frame(self.viewAppsWin)
        buttonFrame.grid(row = 1, column = 0, columnspan = 6)

        backButton = Button(buttonFrame, text = "Back",width = 15, command = self.Back_View_apps)
        backButton.grid(row = 0,column = 0 ,  sticky = E)
        acceptButton = Button(buttonFrame, text = "Accept",width = 15)#, command =self.acceptApplicant)
        acceptButton.grid(row = 0,column = 3,  sticky = E)
        rejectButton = Button(buttonFrame, text = "Reject",width = 15)#, command =self.rejectApplicant)
        rejectButton.grid(row = 0,column = 4,  sticky = E)
        
    def App_report(self):
        self.applicationReportWin = Toplevel()
        self.chooseFuncWin.withdraw()
        self.applicationReportWin.title("Application Report")

        #totalFrame + label
        totalInfoF = Frame(self.applicationReportWin)
        totalInfoF.grid(row = 0, column = 0, columnspan = 6)

 #      self.totApps = SQL query to get the application total
 #      self.totApps = SQL query to get total of accepted applications 
        totAppLab = Label(totalInfoF, text="applications in total, accepted  applications")
        totAppLab.grid(row =0, column = 0) 

        #projectInfo Frame
        self.projectInfoF = Frame(self.applicationReportWin,bd= 3,bg="black")
        self.projectInfoF.grid(row = 1, column = 0, columnspan = 6)

        projectLab = Label(self.projectInfoF, text="Project",width=20,bg="Light Blue")
        projectLab.grid(row =0, column = 0, sticky=W,padx=3,pady=1)

        numLab = Label(self.projectInfoF, text="Number of Applications",width=20,bg="Light Blue")
        numLab.grid(row =0, column = 1, sticky=W,padx=3,pady=1)

        acceptLab = Label(self.projectInfoF, text="Acceptance Rate",width=20,bg="Light Blue")
        acceptLab.grid(row =0, column = 2, sticky=W,padx=3,pady=1)

        top3Lab = Label(self.projectInfoF, text="Top 3 Major",width=20,bg="Light Blue")
        top3Lab.grid(row =0, column = 3, sticky=W,padx=3,pady=1)

        #SQL stuff will provide the info
        appframeCounter=1
        self.projNumAccToplist =[("Project A","24","75%","CS"),("Project B","25","80%","IE/MATH/CS"),("Project C","67","2%","MATH/PHYSICS/ATOM"),("Project F","5","90%","CS/HIST/SOC")]
        for tup in self.projNumAccToplist:
            projectName=tup[0]
            numOfApplicants=tup[1]
            acceptrate=tup[2]
            top3Major=tup[3]
            lab=Label(self.projectInfoF, text =str(projectName), width=20)
            lab.grid(row=appframeCounter,column=0,sticky=W,padx=3,pady=1)
            lab=Label(self.projectInfoF, text =str(numOfApplicants), width=20)
            lab.grid(row=appframeCounter,column=1,sticky=W,padx=3,pady=1)
            lab=Label(self.projectInfoF, text =str(acceptrate), width=20)
            lab.grid(row=appframeCounter,column=2,sticky=W,padx=3,pady=1)
            lab=Label(self.projectInfoF, text =str(top3Major), width=20)
            lab.grid(row=appframeCounter,column=3,sticky=W,padx=3,pady=1)
            appframeCounter=appframeCounter+1

        #the back button
        buttonFrame = Frame(self.applicationReportWin)
        buttonFrame.grid(row = 2, column = 0, columnspan = 6)

        backButton = Button(buttonFrame, text = "Back",width = 15, command = self.Back_App_report)
        backButton.grid(row = 0,column = 0 ,  sticky = E)
        

    def Add_proj(self):
        #called by
        self.chooseFuncWin.withdraw()
        self.addProjectWin = Toplevel() 
        self.addProjectWin.title("Add a Project")
        print("admin add project")
        self.projInfoFrame = Frame(self.addProjectWin)
        self.projInfoFrame.grid(row = 0, column = 0, columnspan = 6)
        #LABELS
        projNameLab = Label(self.projInfoFrame, text="Project Name:")
        projNameLab.grid(row =0, column = 0)
        advisorLab = Label(self.projInfoFrame, text="Advisor:")
        advisorLab.grid(row=1, column=0)
        advisorEmLab = Label(self.projInfoFrame, text="Advisor Email:")
        advisorEmLab.grid(row=2, column=0)
        descriptLab = Label(self.projInfoFrame, text="Description:")
        descriptLab.grid(row=3, column=0)
        categoryLab = Label(self.projInfoFrame, text="Category:")
        categoryLab.grid(row=4, column=0)

    
 
        #ENTRIES
        self.projName = StringVar()
        projNameEnt = Entry(self.projInfoFrame, width =30, textvariable = self.projName)
        projNameEnt.grid(row=0, column =1)
        self.advisor = StringVar()
        advisorEnt = Entry(self.projInfoFrame, width =30, textvariable = self.advisor)
        advisorEnt.grid(row=1, column=1)
        self.advisorEm = StringVar()
        advisorEmEnt = Entry(self.projInfoFrame, width =30, textvariable = self.advisorEm)
        advisorEmEnt.grid(row=2, column=1)
        self.descript = StringVar()
        descriptEnt = Entry(self.projInfoFrame, width =30, textvariable = self.descript)
        descriptEnt.grid(row=3, column=1)
        #CATEGORY
        self.ProjPageCat=StringVar()
        self.ProjPageCat.set("Please Select")
        #USE SQL to call list of cat names called self.catlist
        self.catlist3=["Add cat1 here"," Add cat2 here", "No Requirement"]

        ########
        
        self.ProjPageCatdrop=OptionMenu(self.projInfoFrame,self.ProjPageCat,*self.catlist3)
        self.ProjPageCatdrop.grid(row=4,column=1)
        self.AddProj_AddCatBut=Button(self.projInfoFrame, text="Add Category", width = 15, command = self.CreateProjAddCat)
        self.AddProj_AddCatBut.grid(row=4,column=2)
        self.ApAcRow=4


        
        projInfoFrame2 = Frame(self.addProjectWin)
        projInfoFrame2.grid(row = 1, column = 0, columnspan = 6)

        desigLab = Label(projInfoFrame2, text="Designation:")
        desigLab.grid(row=0, column=0)
        estNumLab = Label(projInfoFrame2, text="Estimated Number of Students:")
        estNumLab.grid(row=1, column=0)
        majorLab = Label(projInfoFrame2, text="Major Requirement:")
        majorLab.grid(row=2, column=0)
        yearLab = Label(projInfoFrame2, text="Year Requirement:")
        yearLab.grid(row=3, column=0)
        deptLab = Label(projInfoFrame2, text="Department Requirement:")
        deptLab.grid(row=4, column=0)

        
        #DESIGNATION
        self.ProjPageDes=StringVar()
        self.ProjPageDes.set("Please Select")
        #USE SQL to call list of des names called self.deslist
        self.deslist=["Add des1 here"," Add des2 here", "No Requirement"]
        self.ProjPageDesdrop=OptionMenu(projInfoFrame2,self.ProjPageDes,*self.deslist)
        self.ProjPageDesdrop.grid(row=0,column=1)
        
        # EWstimated NUmber of Students
        self.estNum = StringVar()
        estNumEnt = Entry(projInfoFrame2, width =30, textvariable = self.estNum)
        estNumEnt.grid(row=1, column=1)
        #MAJOR
        self.ProjPageMaj=StringVar()
        self.ProjPageMaj.set("Please Select")
        #USE SQL to call list of major names called self.majlist
        self.majlist=["Add maj1 here"," Add maj2 here", "No Requirement"]
        self.ProjPageMajdrop=OptionMenu(projInfoFrame2,self.ProjPageMaj,*self.majlist)
        self.ProjPageMajdrop.grid(row=2,column=1)
        #YEAR
        self.ProjPageYr=StringVar()
        self.ProjPageYr.set("Please Select")
        self.yrlist=["Freshman","Sophomore","Junior","Senior", "No Requirement"]
        self.ProjPageYrdrop=OptionMenu(projInfoFrame2,self.ProjPageYr,*self.yrlist)
        self.ProjPageYrdrop.grid(row=3,column=1)
        #DEPARTMENT
        self.ProjPageDept=StringVar()
        self.ProjPageDept.set("Please Select")
        #USE SQL to call list of dept names called self.deptlist
        self.deptlist=["Add dept1 here"," Add dept2 here", "No Requirement"]
        self.ProjPageDeptdrop=OptionMenu(projInfoFrame2,self.ProjPageDept,*self.deptlist)
        self.ProjPageDeptdrop.grid(row=4,column=1)


        backButton = Button(self.addProjectWin, text = "Back",width = 15, command = self.ApBack)
        backButton.grid(row = 10,column = 0 ,  sticky = E)
        
        submitButton = Button(self.addProjectWin, text = "Submit",width = 15)#, command =self.submitNewCourse)
        submitButton.grid(row = 10,column = 1,  sticky = E)
        self.APAClist =[]

    def CreateProjAddCat(self):
        #print("adding a cat for adding a project")
        if self.ProjPageCat.get() == "Please Select":
            return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")

        if self.ApAcRow == 4 : #first run around
            self.APAClist.append(self.ProjPageCat.get())

        if self.ApAcRow > 4: 
            if self.ProjPageCat1.get() == "Please Select":
 #               self.ApAcRow  = self.ApAcRow  - 1
                return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")

            if self.ProjPageCat1.get() not in self.APAClist :
                self.APAClist.append(self.ProjPageCat1.get())

            else:
#                self.ApAcRow = self.ApAcRow - 1
                return messagebox.showerror("OOps!","Please Do not Repeat Categories")

        self.ApAcRow = self.ApAcRow + 1


        self.ProjPageCat1 = StringVar()
        self.ProjPageCat1.set("Please Select")
        
        self.ProjPageCatdrop1 =OptionMenu(self.projInfoFrame, self.ProjPageCat1, *self.catlist3)
        self.ProjPageCatdrop1.grid(row=self.ApAcRow, column =1)

        self.AddProj_AddCatBut.destroy()
        
        self.AddProj_AddCatBut = Button(self.projInfoFrame, text="Add Category", width = 15, command = self.CreateProjAddCat)
        self.AddProj_AddCatBut.grid(row = self.ApAcRow,column = 2)

 
        self.APAClist.append(self.ProjPageCat1.get())

        if self.ApAcRow-4 >= len(self.catlist3): #-1:
          self.AddProj_AddCatBut.config(state="disabled")
          self.FinalApAClist=[]
          for item in self.APAClist:
              if item != "Please Select":
                  self.FinalApAClist.append(item)
          print(self.FinalApAClist)                 
          return messagebox.showerror("OOps!","You have reached the maximum amount of Categories that can be added")
        
        

    def ApBack(self):
        self.ChooseFunc()
        self.addProjectWin.withdraw()

    

        
    def Add_course(self):
        #called by Button "add course" in the choose functionality function

        #self.chooseFunWin.withdraw()

        #creates Add Course window and hides Choose Func window
        self.addCourseWin = Toplevel()
        self.chooseFuncWin.withdraw()
        self.addCourseWin.title("Add a Course")

        #frame to put the Course#/Course Name/Instructor/Designation/Ctaegory/Est Students in 
        self.courseInfoFrame = Frame(self.addCourseWin)
        self.courseInfoFrame.grid(row = 0, column = 0, columnspan = 6)

        #LABELS
        courseNumLab = Label(self.courseInfoFrame, text="Course Number:")
        courseNumLab.grid(row =0, column = 0) 

        courseNameLab = Label(self.courseInfoFrame, text="Course Name:")
        courseNameLab.grid(row =1, column = 0)

        instructorLab = Label(self.courseInfoFrame, text="Instructor:")
        instructorLab.grid(row =2, column = 0)

        designationLab = Label(self.courseInfoFrame, text="Designation:")
        designationLab.grid(row =3, column = 0)

        categoryLab = Label(self.courseInfoFrame, text="Category:")
        categoryLab.grid(row =4, column = 0)

        self.estimatedNumStudentsLab = Label(self.courseInfoFrame, text="Estimated # of students:")
        self.estimatedNumStudentsLab.grid(row =5, column = 0) 
        

        #Entries for labels

        self.newCourseNum = StringVar()
        courseNumEnt =Entry(self.courseInfoFrame, width =30, textvariable = self.newCourseNum)
        courseNumEnt.grid(row=0, column =1)

        self.newCourseName = StringVar()
        courseNameEnt =Entry(self.courseInfoFrame, width =30, textvariable = self.newCourseName)
        courseNameEnt.grid(row=1, column =1)

        self.newInstructor = StringVar()
        newInstructorEnt =Entry(self.courseInfoFrame, width =30, textvariable = self.newInstructor)
        newInstructorEnt.grid(row=2, column =1)

        self.estNumStudents = StringVar()
        self.estNumStudentsEnt =Entry(self.courseInfoFrame, width =30, textvariable = self.estNumStudents)
        self.estNumStudentsEnt.grid(row=5, column =1)

        self.AddCourseCat = StringVar()
        self.AddCourseCat.set("Please Select")
        self.catlist1=["cat1","cat 2", "cat 3", "cat 4"]
        self.AddCC =OptionMenu(self.courseInfoFrame, self.AddCourseCat, *self.catlist1)
        self.AddCC.grid(row=4, column =1)
        self.ACrow=4

        self.ACBut = Button(self.courseInfoFrame, text = "Add Category",width = 15, command = self.Add_Course_Cat)
        self.ACBut.grid(row = 4,column = 2 ,  sticky = E)
        

        self.addCourseDes=StringVar()
        self.addCourseDes.set("Please Select")

        #USE SQL to call list of Designation names called self.deslist
        self.AACDes=StringVar()
        self.AACDes.set("Please Select")
        self.deslist=["Add des1 here"," Add des2 here"]
        self.addCourseDesdrop=OptionMenu(self.courseInfoFrame,self.AACDes,*self.deslist)
        self.addCourseDesdrop.grid(row=3,column=1)

        #Put Buttons in Frame
        self.buttonFrame = Frame(self.addCourseWin)
        self.buttonFrame.grid(row = 1, column = 0, columnspan = 6)

        backButton = Button(self.buttonFrame, text = "Back",width = 15, command = self.Back_Add_course)
        backButton.grid(row = 0,column = 0 ,  sticky = E)
        
        submitButton = Button(self.buttonFrame, text = "Accept",width = 15)#, command =self.submitNewCourse)
        submitButton.grid(row = 0,column = 1,  sticky = E)

        self.totalAClist=[]

    def Add_Course_Cat(self):
        #print("Adding Course")

        if self.AddCourseCat.get() == "Please Select":
            return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")
        
        if self.ACrow == 4 : #first run around
            self.totalAClist.append(self.AddCourseCat.get())

        

 #       self.ACrow=self.ACrow+1
     

        if self.ACrow > 4: 
            if self.AddCourseCat1.get() == "Please Select":
 #               self.ACrow = self.ACrow - 1
                return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")
            
            if self.AddCourseCat1.get() not in self.totalAClist :
                self.totalAClist.append(self.AddCourseCat1.get())

            else:
 #               self.ACrow = self.ACrow - 1
                return messagebox.showerror("OOps!","Please Do not Repeat Categories")

        self.ACrow=self.ACrow+1
        
        

       # print(self.totalAClist)
        
        self.AddCourseCat1 = StringVar()
        self.AddCourseCat1.set("Please Select")
        
        self.AddCC1 =OptionMenu(self.courseInfoFrame, self.AddCourseCat1, *self.catlist1)
        self.AddCC1.grid(row=self.ACrow, column =1)

        self.ACBut.destroy()
        
        self.ACBut = Button(self.courseInfoFrame, text = "Add Category",width = 15, command = self.Add_Course_Cat)
        self.ACBut.grid(row = self.ACrow,column = 2 ,  sticky = E)

        self.estNumStudentsEnt.destroy()

        self.estNumStudents1 = StringVar()
        self.estNumStudents1.set(self.estNumStudents.get())
        
        self.estNumStudentsEnt =Entry(self.courseInfoFrame, width =30, textvariable = self.estNumStudents1)
        self.estNumStudentsEnt.grid(row=self.ACrow+1, column =1)
        
        self.estimatedNumStudentsLab.destroy()
        self.estimatedNumStudentsLab = Label(self.courseInfoFrame, text="Estimated # of students:")
        self.estimatedNumStudentsLab.grid(row =self.ACrow+1, column = 0) 
        

        self.totalAClist.append(self.AddCourseCat1.get())

       # print(self.totalAClist)
       # Not needed actually!!!
        
        if self.ACrow-4 >= len(self.catlist1): #-1:
          self.ACBut.config(state="disabled")
          self.FinalACCatlist=[]
          for item in self.totalAClist:
              if item != "Please Select":
                  self.FinalACCatlist.append(item)
          print(self.FinalACCatlist)                 
          return messagebox.showerror("OOps!","You have reached the maximum amount of Categories that can be added")

    
    

win = Tk()
app = CS4400(win)
win.mainloop()
