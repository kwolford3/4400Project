from tkinter import *
import pymysql
import datetime
import os
from re import findall


#Check for scrollbar needs: Popular Projects and Application Report
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
        username = self.user.get()
        password =self.passw.get()
        
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql="SELECT Flag from User where UserName =%s and Password=%s"
        n =cursor.execute(sql,(username,password))
        
        self.flagRet=cursor.fetchall()

        cursor.close()
        db.commit()
        db.close()
   
 #       print(self.flagRet)
        
        if n == 1: 
 #           messagebox.showerror("Login Successful!","Login Succesful")
            print("login successful")
            
            
	#if student main, if admin choose functionality
            for tup in self.flagRet:
                self.flag = tup[0]
               
            if self.flag == "Student":
                 self.Main_page()
            if self.flag == "Admin":
                
                self.ChooseFunc()
        else:
            return messagebox.showerror("Error","Credentials are invalid")



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
        self.logOutBut = Button(self.chooseFuncWin, text="Log Out", command=self.Log_Out)#need to add a command here
        self.logOutBut.grid(row=6,column=0)

    def Log_Out(self):
        self.chooseFuncWin.withdraw()
        return messagebox.showerror("Logged Out!","You are now Logged Out")
        


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
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT Pname, Count(Pname) FROM Application GROUP BY Pname ORDER BY Count(Pname) DESC LIMIT 10;"
        cursor.execute(sql)
        self.projMajYearStatlist=cursor.fetchall()
        print(self.projMajYearStatlist)
        #self.projMajYearStatlist =[("Project A","34"),("Project B","55"),("Project C","67"),("Project F","69")]
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
        #print("Registered")
       
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
        

    def RegisterCheck(self):
      
        username = self.user.get()
        userEmail = self.email.get()
        password =self.passw.get()
        confirmPass = self.conf.get()

        if "@gatech.edu" != userEmail[-11::]:
            return messagebox.showerror("Error","Enter Georga Tech Email Address")
        if username == "" or userEmail == "" or password == "" or confirmPass == "":
            return messagebox.showerror("Error","complete all entry fields")
        if password != confirmPass:
            return messagebox.showerror("Error","Passwords Do Not Match")

        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql="INSERT INTO User(UserName, Password, Flag) VALUES (%s, %s,%s)"
        try:
            n =cursor.execute(sql,(username,password,"Student"))
            cursor.close()
            db.commit()
            db.close()
            print("added to user")
            # may need to seperate into two try statemments and add database rollback
            db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
            cursor = db.cursor()
            sql = "INSERT into Student (UserName,GtEmail) VALUES (%s,%s)"
            n =cursor.execute(sql,(username,userEmail))
            print("added to student")
            cursor.close()
            db.commit()
            db.close()
            

        except:
            cursor.close()
            db.commit()
            db.close()
            return messagebox.showerror("Error","DataBase rejected you!!! Try Again")

 
        
        self.registerWin.destroy()
        self.Main_page() #ONLY RUN IF A SUCCESFUL REGISTER
        
    def Main_page(self):
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT Mname from Major"
        cursor.execute(sql)
        self.majors=cursor.fetchall()
        self.majlist=[]
        for tup in self.majors:
            self.majlist.append(tup[0])
        cursor.close()
        db.commit()
        db.close()

        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT Catname from Category"
        cursor.execute(sql)
        self.cats=cursor.fetchall()
        self.catlist=[]
        for tup in self.cats:
            self.catlist.append(tup[0])
        cursor.close()
        db.commit()
        db.close()

        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT DesigName from Desig"
        cursor.execute(sql)
        self.des=cursor.fetchall()
        self.deslist=[]
        for tup in self.des:
            self.deslist.append(tup[0])
        cursor.close()
        db.commit()
        db.close()

        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT Cname from Course"
        cursor.execute(sql)
        self.C=cursor.fetchall()
        self.Clist=[]
        for tup in self.C:
            ntup=(tup[0],"Course")
            self.Clist.append(ntup)
        #print(self.Clist)           
        cursor.close()
        db.commit()
        db.close()

        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT Pname from Project"
        cursor.execute(sql)
        self.P=cursor.fetchall()
        self.Plist=[]
        for tup in self.P:
            ntup=(tup[0],"Project")
            self.Plist.append(ntup)           
        cursor.close()
        db.commit()
        db.close()

        self.CPlist=self.Plist+self.Clist # NEED A SCROLL BAR!!!!!!!!!!!
        #print(self.CPlist)
        #called by ME Page
        #also called by a succesfull login page
        self.loginWin.withdraw()
        #self.registerWin.withdraw()
        self.Main_pageWin1 = Toplevel()
        self.Main_pageWin1.title("Main Page")
        self.Main_pageWin1.minsize(width = 1000, height=500)
        #added for scrollbar
        self.Main_pageWin2 = Canvas(self.Main_pageWin1, bg = 'white')
        self.Main_pageWin2.pack(side = RIGHT, fill = BOTH, expand = True)
        print("canvas packed")
        self.Main_pageWin = Frame(self.Main_pageWin2, bd=3, bg='white')
        self.canvas_frame = self.Main_pageWin2.create_window((0,0), window=self.Main_pageWin, anchor = NW)
 
        self.Main_pageWin.bind("<Configure>", self.OnFrameConfigure)
        self.Main_pageWin2.bind('<Configure>', self.FrameWidth)
        scroll = Scrollbar(self.Main_pageWin2, orient = "vertical", 
            command = self.Main_pageWin2.yview)
        scroll.pack(side = RIGHT, fill = Y)
        self.Main_pageWin2.config(yscrollcommand = scroll.set)
        
        #end of scrollbar
        
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
        
 #       self.deslist=["Add des1 here"," Add des2 here"]
        self.MainPageDesdrop=OptionMenu(self.Main_pageWin,self.MainPageDes,*self.deslist)
        self.MainPageDesdrop.grid(row=2,column=1)

        MainPageLabMaj = Label(self.Main_pageWin,text="Major:")
        MainPageLabMaj.grid(row=3,column=0)
        #print("ran")
        self.MainPageMaj=StringVar()
        self.MainPageMaj.set("Please Select")
        
 #       self.majlist=["Add maj1 here"," Add maj2 here"]
        self.MainPageMajdrop=OptionMenu(self.Main_pageWin,self.MainPageMaj,*self.majlist)
        self.MainPageMajdrop.grid(row=3,column=1)

        MainPageLabYear = Label(self.Main_pageWin,text="Year:")
        MainPageLabYear.grid(row=4,column=0)
        #print("ran")
        self.MainPageYear=StringVar()
        self.MainPageYear.set("Please Select")
        
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
 #       self.canvasframe
        #Course Project List
        
        
 
# 
        ##end of scroll
        self.CPframe=Frame(self.Main_pageWin,bd= 3,bg="black")
        self.CPframe.grid(row=6, column=0,columnspan= 5)
        MPCPlab1= Label(self.CPframe, text ="Name", width=70,bg="Light Blue")
        MPCPlab1.grid(row=0,column=0,sticky=W,padx=3,pady=1)
        MPCPlab2= Label(self.CPframe, text ="Type",width=20,bg="Light Blue")
        MPCPlab2.grid(row=0,column=1,sticky=W,pady=1)
        
        #pull al list of all courses anf projects here will need SQL
        CPframeCounter=1
        print("we are here")              
        #self.CPlist =[("Project A","Project"),("Project B","Project"),("Course A", "Course"),("COurse B","Course"),("Project Q","Project")]
        for tup in self.CPlist:
            Name=tup[0]
            typ=tup[1]
            pair= (Name,typ)
            self.SelectBut=Button(self.CPframe, text =str(Name), width=70 ,command = lambda pair= pair: self.view(pair))
            self.SelectBut.grid(row=CPframeCounter,column=0,sticky=W,padx=3,pady=1)
            self.lab=Label(self.CPframe, text =str(typ), width=20)
            self.lab.grid(row=CPframeCounter,column=1,sticky=W,pady=1)
            CPframeCounter=CPframeCounter+1
    
        
    def view(self,P): #,T):
       # print("View")
        Name = P[0]
        typ = P[1]
        print(Name +" Is A " + typ ) # Prints Name of Project or sourse selected
        if typ == "Project":
            print("is a Project, run view Project")
 #           self.ProjOfInterest=Name
            self.View_Project(Name)
            
        if typ == "Course":
            print("is a Course, run View Course")
 #           self.CourseOfInterest=Name
            self.View_course(Name)
            
            
            
        
        # need to figure out if selected reult is a project or a course
        
        
 #       will need to check if selected button is a course or a project and then run the respective view course or view project button below


    def View_Project(self,select):
        self.projname = select
        #called by Main_page (by selecting a project)
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        # This is not right, beet fo do a full outer join of these three tables
 #       sql = "SELECT Aname, Description, DesigName, Catname, Requirement, Num_Students FROM Project NATURAL JOIN Proj_Cat NATURAL JOIN Requires where Pname =%s"
        sql = "SELECT p.Aname, p.Description, p.DesigName, c.Catname, r.requirement, p.Num_Students from Project p Left JOIN Proj_Cat c on p.Pname = c.Pname Left JOIN Requires r on r.Pname = p.Pname where p.Pname=%s"
        cursor.execute(sql,(select))
        self.projinfo=cursor.fetchall()
        cursor.close()
        db.commit()
        db.close()
        count=0
        count1 =0
 #       print(self.projinfo)
        require=""
        cat = ""
        for item in self.projinfo:
            count=count+1
            if item[4] == None:
                require= "None"
            elif count == 1:
                if item[4] not in require:
                    require =require+item[4]
                
            else:
                if item[4] not in require:
                    require=require+", "+item[4]

        for item in self.projinfo:
            count1=count1+1
            #if item[4] == None:
#                require= "None"
            if count1 == 1:
                if item[3] not in cat:
                    cat =cat+item[3]
                
            else:
                if item[3] not in cat:
                    cat=cat+", "+item[3]
                
                
 #       print(require)
 #       print(cat)
        
        
            
            

        #creating the View Project window and hiding the Main Page window
        self.viewProjWin = Toplevel()
        self.Main_pageWin1.withdraw()
        self.viewProjWin.title("View Project: "+str(select))
        
        #creating lefthand side labels (NO SQL) and buttons within View Project window
        advisorLab = Label(self.viewProjWin, text="Advisor:")
        advisorLab.grid(row=1,column=0)
        descriptionLab = Label(self.viewProjWin, text="Description:")#, width=60)
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
        self.applyBut = Button(self.viewProjWin, text="Apply",command=self.Apply_Button)
        self.applyBut.grid(row=7,column=1)

        #creating title and righthand side labels (SQL INCLUDED/NEEDED)
        #need to insert SQL statements to retrieve actual information
        self.SQLprojNameLab = Label(self.viewProjWin,text=select)  #"Insert Proj Name SQL")
        self.SQLprojNameLab.grid(row=0,column=0,columnspan=2)
        self.SQLadvisor = Label(self.viewProjWin, text=self.projinfo[0][0])
        self.SQLadvisor.grid(row=1,column=1)
        self.SQLdescription = Message(self.viewProjWin, text=self.projinfo[0][1], width=300)
        self.SQLdescription.grid(row=2,column=1)
        self.SQLdesignation = Label(self.viewProjWin, text=self.projinfo[0][2])
        self.SQLdesignation.grid(row=3,column=1)
        self.SQLcategory = Label(self.viewProjWin, text=cat)#self.projinfo[0][3])
        self.SQLcategory.grid(row=4,column=1)
        self.SQLrequire = Label(self.viewProjWin, text=require) #self.projinfo[0][4])
        self.SQLrequire.grid(row=5,column=1)
        self.SQLnumStud = Label(self.viewProjWin, text=str(self.projinfo[0][5]))
        self.SQLnumStud.grid(row=6,column=1)


    def Apply_Button(self):
        print("applied")
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        proj_name = self.projname
        print("Applying to: ",proj_name)
        username = self.user.get()
        print("User is: ",username)
        sql_email = "SELECT Year,GtEmail,Mname FROM Student WHERE UserName = %s;"
        cursor.execute(sql_email, (username))
        db.commit()
        info = cursor.fetchall()
        year = info[0][0]
        email = info[0][1]
        major = info[0][2]
        cursor.close()
        print("User's year is: ",year)
        print("User's email is: ",email)
        print("User's major is: ",major)
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql_dept = "SELECT Dname FROM Major WHERE Mname = %s;"
        cursor.execute(sql_dept, (major))
        depts = cursor.fetchall()
        dept = depts[0][0]
        student_info = [year,major,dept]
        print("Dept of User's major is: ",dept)
        cursor.close()
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql_require = "SELECT Requirement FROM Requires WHERE Pname = %s;"
        cursor.execute(sql_require, (proj_name))
        requirements = cursor.fetchall()
        print(requirements)
        for req in requirements:
            if req[0] == "":
                pass
            else:
                if req[0] in student_info:
                    pass
                else:
                    messagebox.showerror("Requirement Needed","Sorry, you don't meet the requirements for this project.")
                    return("Done")        
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql_insert = "INSERT INTO Application(Date,Pname,GtEmail) VALUES (%s,%s,%s);"
        date = datetime.datetime.now()
        cursor.execute(sql_insert,("%s-%s-%s" %(date.year,date.month,date.day),proj_name,email))
        db.commit()
        cursor.close()
        messagebox.showinfo("Success","You have applied to %s" %(proj_name))
        print("insert complete")



    def Apply_Filter(self):
       # SEARCHIN IS CASE SENSITIVE!!!!
       # print("apply filter")
        thelist=[]
        final =[]
 #       print(self.MainPageRow)
        if self. MainPageRow == 0:
            thelist.append(self.MainPageCat.get())
        else:
            self.CatTempList.append(self.MainPageCat1.get())
            thelist = thelist+self.CatTempList
        for cat in thelist:
            if cat not in final and cat != "Please Select":
                final.append(cat)

        title = self.MPEntry.get()
        year = self.MainPageYear.get() # requirement
        if year == "Please Select":
            year=""
        major= self.MainPageMaj.get() # requirement
        if major == "Please Select":
            major=""
        des= self.MainPageDes.get()
        if des == "Please Select":
            des =""
        rb = self.MainPageRB.get()
        if rb == "":
            rb="Both"
        #print(title, year, major, des,rb, final)
        if major != "":
            sql = "SELECT m.Dname FROM `Major` m WHERE m.Mname=%s"
            db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
            cursor = db.cursor()
            cursor.execute(sql,(major))
            self.dept=cursor.fetchall()
            cursor.close()
            db.commit()
            db.close()
            #print(self.dept)
            dept = self.dept[0][0]
            #print(dept)

        else:
            dept = ""
        #print(title, year, major, des,rb, final)

        updated=[]
        updated1=[]
        winner =[]

        if rb== "Project" or rb =="Both":
            #print("running fo project and both")
       
            sql = "SELECT p.Pname, p.DesigName, c.Catname, r.requirement from Project p Left JOIN Proj_Cat c on p.Pname = c.Pname Left JOIN Requires r on r.Pname = p.Pname"
            db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
            cursor = db.cursor()
            cursor.execute(sql)
            self.projstat=cursor.fetchall()
            cursor.close()
            db.commit()
            db.close()
           
            
            for ntup in self.projstat:
                if ntup[0]==title or title== "":
                    if ntup[1]==des or des== "":
                        if ntup[2] in final or final == []:
                            if ntup[3] == year or ntup[3] == major or ntup[3] == dept or ntup[3]== None or (major == "" and year ==""): # what if there is no major or yer listed
                                updated.append(ntup)
            #print(updated)
                                
            for item in updated:
                if (item[0],"Project") not in winner:
                    winner.append((item[0],"Project"))

            #print(winner)
            

                
        if rb=="Course" or rb =="Both":
            sql = "SELECT c.Cname, c.DesigName, z.Catname from Course c Left JOIN Course_Cat z on z.Cnum = c.Cnum"
            db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
            cursor = db.cursor()
            cursor.execute(sql)
            self.coursestat=cursor.fetchall()
            cursor.close()
            db.commit()
            db.close()
           
            
            for ntup in self.coursestat:
                if ntup[0]==title or title== "":
                    if ntup[1]==des or des== "":
                        if ntup[2] in final or final == []:
#                            if ntup[3] == year or ntup[3] == major or ntup[3] == dept or ntup[3]== None or (major == "" and year ==""): # what if there is no major or yer listed
                                updated1.append(ntup)
           # print("here:  ", updated1)

            for item in updated1:
                if (item[0],"Course") not in winner:
                    winner.append((item[0],"Course"))

            #print(winner)

        

        #Course Project List
        self.CPframe.destroy()   
        self.CPframe=Frame(self.Main_pageWin,bd= 3,bg="black")
        self.CPframe.grid(row=self.MainPageRow+6, column=0,columnspan= 5)
        MPCPlab1= Label(self.CPframe, text ="Name", width=70,bg="Light Blue")
        MPCPlab1.grid(row=0,column=0,sticky=W,padx=3,pady=1)
        MPCPlab2= Label(self.CPframe, text ="Type",width=20,bg="Light Blue")
        MPCPlab2.grid(row=0,column=1,sticky=W,pady=1)
        #pull al list of all courses anf projects here will need SQL
        CPframeCounter=1
        for tup in winner:
            Name=tup[0]
            typ=tup[1]
            pair=(Name,typ)
            
            self.SelectBut=Button(self.CPframe, text =str(Name), width=70, command = lambda pair= pair: self.view(pair))
            self.SelectBut.grid(row=CPframeCounter,column=0,sticky=W,padx=3,pady=1)
            self.lab=Label(self.CPframe, text =str(typ), width=20)
            self.lab.grid(row=CPframeCounter,column=1,sticky=W,pady=1)
            CPframeCounter=CPframeCounter+1


        if winner == []:
            text = "There are No Matches to your search, Please Note: Title is CASE SENSITIVE "
            return messagebox.showerror("OOPS",text)
        
    def Reset_Filter(self):
        print("Reset Filter")
        self.Main_pageWin1.destroy()
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
            
        
        self.Main_pageWin1.destroy()
 
        
 #       self.Main_pageWin = Toplevel()
#        self.Main_pageWin.title("Main Page")

        self.Main_pageWin1 = Toplevel()
        self.Main_pageWin1.title("Main Page")
	self.Main_pageWin1.minsize(width = 1000, height=500)
        #added for scrollbar
        self.Main_pageWin2 = Canvas(self.Main_pageWin1, bg = 'white')
        self.Main_pageWin2.pack(side = RIGHT, fill = BOTH, expand = True)
        print("canvas packed")
        self.Main_pageWin = Frame(self.Main_pageWin2, bd=3, bg='white')
        self.canvas_frame = self.Main_pageWin2.create_window((0,0), window=self.Main_pageWin, anchor = NW)
 
        self.Main_pageWin.bind("<Configure>", self.OnFrameConfigure)
        self.Main_pageWin2.bind('<Configure>', self.FrameWidth)
        scroll = Scrollbar(self.Main_pageWin2, orient = "vertical", 
            command = self.Main_pageWin2.yview)
        scroll.pack(side = RIGHT, fill = Y)
        self.Main_pageWin2.config(yscrollcommand = scroll.set)
        

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
        self.MainPageDes.set(self.MainPageDes.get())
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
            pair=(Name,typ)
            
            self.SelectBut=Button(self.CPframe, text =str(Name), width=70, command = lambda pair= pair: self.view(pair))
            self.SelectBut.grid(row=CPframeCounter,column=0,sticky=W,padx=3,pady=1)
            self.lab=Label(self.CPframe, text =str(typ), width=20)
            self.lab.grid(row=CPframeCounter,column=1,sticky=W,pady=1)
            CPframeCounter=CPframeCounter+1

    
    def Me_page(self):
        #called by
        #Creates ME window
        #destroy previous window
        self.Main_pageWin1.withdraw()
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

    def dept(self):
        #sets department name on Edit Profile page
        major = self.EditPageMaj.get()
        year = self.EditPageYr.get()
        username = self.user.get()
        if major == "Please Select" or year == "Please Select":
            messagebox.showerror("Invalid Selection","Please fill out both the 'Major' and 'Year' fields.")
            return("Done")
        else:
            pass
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT Dname from Major where Mname = %s"
        cursor.execute(sql,major)
        dlist = cursor.fetchall()
        dept = dlist[0][0]
        cursor.close()
        db.commit()
        db.close()
        self.EditPageDept.set(dept)
        
        #updates Year and Major after student changes it on Edit Profile page
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "UPDATE Student SET Mname=%s,Year=%s WHERE UserName = %s"
        cursor.execute(sql,(major,year,username))
        cursor.close()
        db.commit()
        db.close()
        print("Done updating Dept; Major and Year changes submitted to database")


    def Edit_profile(self):
        #gets list of all majors
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT Mname from Major"
        cursor.execute(sql)
        self.majors=cursor.fetchall()
        self.majlist=[]
        for tup in self.majors:
            self.majlist.append(tup[0])
        cursor.close()
        db.commit()
        db.close()

        #creates Edit Proile Page; called by Me Page
        self.meWin.withdraw()
        self.editWin = Toplevel()
        self.editWin.title("Edit Profile")
        majorLab= Label(self.editWin,text="Major:")
        majorLab.grid(row=0,column=0)
        yearLab= Label(self.editWin,text="Year:")
        yearLab.grid(row=1,column=0)
        deptLab= Label(self.editWin,text="Department:")
        deptLab.grid(row=2,column=0)
        self.EditPageDept = StringVar()
        self.SQLdeptLab = Label(self.editWin,textvariable = self.EditPageDept)
        self.SQLdeptLab.grid(row=2,column=1)

        self.EditPageMaj=StringVar()
        self.EditPageMaj.set("Please Select")        
        self.EditPageMajdrop=OptionMenu(self.editWin,self.EditPageMaj,*self.majlist)
        self.EditPageMajdrop.grid(row=0,column=1)
        self.EditPageYr=StringVar()
        self.EditPageYr.set("Please Select")
        self.yrlist=["Freshman","Sophomore","Junior","Senior"]
        self.EditPageYrdrop=OptionMenu(self.editWin,self.EditPageYr,*self.yrlist)
        self.EditPageYrdrop.grid(row=1,column=1)

        self.backBut = Button(self.editWin, text = "Back", command = self.EditBack)
        self.backBut.grid(row=3, column=0)
        self.editWin.deiconify()
        self.submitBut = Button(self.editWin, text = "Submit Changes",command=self.dept)
        self.submitBut.grid(row=3,column=1)
        
    
        
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
        username = self.user.get()
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql="SELECT Student.GtEmail from Student where UserName = %s"
        self.cursor.execute(sql,(username))
        self.email=self.cursor.fetchall()
        self.cursor.close()
        db.commit()
        db.close()
        #print(self.email[0])
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql= "SELECT a.Date, a.Pname, a.Status from Application a where GtEmail=%s"
        self.cursor.execute(sql,(self.email[0]))
        self.projects=self.cursor.fetchall()
        self.cursor.close()
        db.commit()
        db.close()            
        #self.MyAppList=[("10/11/12","Project A","Pending"),("1/11/16","Project 9","Accepted"),("12/12/95","Project 9","Rejected")]
        MyAppCounter= 1
        for tup in self.projects:
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

    def View_course(self,select):
       
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT c.Instructor, c.CnumStud, c.DesigName, z.Catname from Course c Left JOIN Course_Cat z on z.Cnum = c.Cnum where c.Cname=%s"
        cursor.execute(sql,(select))
        self.courseListinfo=cursor.fetchall()
        cursor.close()
        db.commit()
        db.close()
       
        count1 =0
        print(self.courseListinfo)
        # need to check if a course must have a category associated with it
       
        cat = ""
        #if self.courseListinfo[0][
        if self.courseListinfo[0][3] == None:
            cat = "None"
        else:
            for item in self.courseListinfo:
                count1=count1+1
            
                if count1 == 1:
                    if item[3] not in cat:
                        cat =cat+item[3]
                
                else:
                    if item[3] not in cat:
                        cat=cat+", "+item[3]
                
                
        self.ViewCourseWin=Toplevel()
        self.Main_pageWin1.withdraw()
        
        self.ViewCourseWin.title("View Course: "+str(select))
        #will be called from selections based on sql and main page
        #self.courseListinfo=("Example Course Name","Example Instructor","Example Designation", "Example Cat", "##")
        
        VCLab1 =Label(self.ViewCourseWin, text="Course Name:",bg="Light Blue")
        VCLab1.grid(row = 0, column=0,padx = 5, pady=5 )
        VCName =Label(self.ViewCourseWin, text=select)#self.courseListinfo[0])
        VCName.grid(row = 0, column=1,padx = 5, pady=5)
        
        VCLab1 =Label(self.ViewCourseWin, text="Instructor:",bg="Light Blue")
        VCLab1.grid(row = 1, column=0,padx = 5, pady=5 )
        VCInst =Label(self.ViewCourseWin, text=self.courseListinfo[0][0])
        VCInst.grid(row = 1, column=1,padx = 5, pady=5 )
        
        VCLab2 =Label(self.ViewCourseWin, text="Designation:",bg="Light Blue")
        VCLab2.grid(row = 2, column=0,padx = 5, pady=5 )
        VCDes =Label(self.ViewCourseWin, text=self.courseListinfo[0][2])
        VCDes.grid(row = 2, column=1,padx = 5, pady=5 )

        VCLab3 =Label(self.ViewCourseWin, text="Category",bg="Light Blue")
        VCLab3.grid(row = 3, column=0,padx = 5, pady=5 )
        VCCat =Label(self.ViewCourseWin, text=cat) #self.courseListinfo[3])
        VCCat.grid(row = 3, column=1,padx = 5, pady=5 )

        VCLab4 =Label(self.ViewCourseWin, text="Estimatied Number of Students",bg="Light Blue")
        VCLab4.grid(row = 4, column=0,padx = 5, pady=5 )
        VCNum =Label(self.ViewCourseWin, text=self.courseListinfo[0][1])
        VCNum.grid(row = 4, column=1,padx = 5, pady=5 )

        VCBackBut=Button(self.ViewCourseWin, text="Back", command=self.VCBack)
        VCBackBut.grid(row=5, column=0)

    def VCBack(self):
        self.ViewCourseWin.withdraw()
        self.Main_page()
        

    def View_apps(self):
        #called by the "View applications button" in the Choose Functionality Pgae
        #self.projMajYearStatlist =[]
        
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT p.Pname, s.Mname, s.Year, a.Status, a.GtEmail from Application a JOIN Project p on a.Pname = p.Pname JOIN Student s on a.GtEmail = s.GtEmail"
        cursor.execute(sql)
        self.applications=cursor.fetchall()

        cursor.close()
        db.commit()
        db.close()

        #creates View Apps window
        self.viewAppsWin = Toplevel()
        self.chooseFuncWin.withdraw()
        self.viewAppsWin.title("Application")

        #frame to put the Apllications in
        self.projectFrame = Frame(self.viewAppsWin,bd= 3,bg="black")
        self.projectFrame.grid(row = 0, column = 0, columnspan = 6)

        #Labels for Project, Applicant Major/Year, Status
        projectLabel =Label(self.projectFrame, text="Project",width = 30,bg="Light Blue")
        projectLabel.grid(row = 0, column=1,sticky=W,padx=3,pady=1)

        appMajorLabel =Label(self.projectFrame, text="Applicant Major",width = 20,bg="Light Blue")
        appMajorLabel.grid(row = 0, column=2,sticky=W,padx=3,pady=1)

        appYearLabel =Label(self.projectFrame, text="Applicant Year",width = 20,bg="Light Blue")
        appYearLabel.grid(row = 0, column=3,sticky=W,padx=3,pady=1)

        statusLabel =Label(self.projectFrame, text="Status",width = 20,bg="Light Blue")
        statusLabel.grid(row = 0, column=4,sticky=W,padx=3,pady=1)

        #pull al list of all Project, Applicant Major/Year, Status
        projectframeCounter=1
        pendingRowList = []
        self.pendingTuple = []
        for tup in self.applications:
            projectName=tup[0]
            applicantMajor=tup[1]
            applicantYear=tup[2]
            applicantStatus=tup[3]
            applicantEmail = tup[4]
            lab=Label(self.projectFrame, text =str(projectName), width=30)
            lab.grid(row=projectframeCounter,column=1,sticky=W,padx=3,pady=1)
            lab=Label(self.projectFrame, text =str(applicantMajor), width=20)
            lab.grid(row=projectframeCounter,column=2,sticky=W,padx=3,pady=1)
            lab=Label(self.projectFrame, text =str(applicantYear), width=20)
            lab.grid(row=projectframeCounter,column=3,sticky=W,padx=3,pady=1)
            lab=Label(self.projectFrame, text =str(applicantStatus), width=20)
            lab.grid(row=projectframeCounter,column=4,sticky=W,padx=3,pady=1)
            if applicantStatus == "Pending":
                pendingRowList.append(projectframeCounter)
                tupsNeeded = (projectframeCounter,projectName,applicantMajor,applicantYear,applicantStatus, applicantEmail)
                self.pendingTuple.append(tupsNeeded)
            projectframeCounter=projectframeCounter+1


        #Radio BUttons
        self.variableRBut = IntVar()
        for i in pendingRowList:
            self.viewApps=IntVar()
            self.ProjRButton= Radiobutton(self.projectFrame, variable=self.variableRBut, value=i)
            self.ProjRButton.grid(row=i,column=0)

        
        #creates frame for Back Accept Reject Button
        buttonFrame = Frame(self.viewAppsWin)
        buttonFrame.grid(row = 1, column = 0, columnspan = 6)

        backButton = Button(buttonFrame, text = "Back",width = 15, command = self.Back_View_apps)
        backButton.grid(row = 0,column = 0 ,  sticky = E)
        acceptButton = Button(buttonFrame, text = "Accept",width = 15, command =self.Accept_Apps)
        acceptButton.grid(row = 0,column = 3,  sticky = E)
        rejectButton = Button(buttonFrame, text = "Reject",width = 15, command =self.Reject_Apps)
        rejectButton.grid(row = 0,column = 4,  sticky = E)

    def Accept_Apps(self):
        value = self.variableRBut.get()
        p = "Pending"
        z= "Accepted"
        for i in self.pendingTuple:
            if value == i[0]:
                print(i[0])
                pName = i[1]
                aEmail = i[5]
                db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
                cursor = db.cursor()
                sql = "UPDATE Application a SET a.Status = %s WHERE a.Pname = %s and a.GtEmail = %s and a.Status = %s"   
                cursor.execute(sql,(z,pName,aEmail,p))
                cursor.close()
                db.commit()
                db.close()
                self.viewAppsWin.withdraw() 
                self.View_apps()
                    

    def Reject_Apps(self):
        value = self.variableRBut.get()
        p = "Pending"
        z= "Rejected"
        for i in self.pendingTuple:
            if value == i[0]:
                print(i[0])
                pName = i[1]
                aEmail = i[5]
                db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
                cursor = db.cursor()
                sql = "UPDATE Application a SET a.Status = %s WHERE a.Pname = %s and a.GtEmail = %s and a.Status = %s"   
                cursor.execute(sql,(z,pName,aEmail,p))
                cursor.close()
                db.commit()
                db.close()
                self.viewAppsWin.withdraw() 
                self.View_apps()
        
    def App_report(self):
        self.applicationReportWin = Toplevel()
        self.chooseFuncWin.withdraw()
        self.applicationReportWin.title("Application Report")
        self.applicationReportWin.minsize(width = 700, height=500)
        #totalFrame + label
        #totalInfoF = Frame(self.applicationReportWin)
        #totalInfoF.grid(row = 0, column = 0, columnspan = 6)

        #added for scrollbar
        self.canvas = Canvas(self.applicationReportWin, bg = 'white')
        self.canvas.pack(side = RIGHT, fill = BOTH, expand = True)
        print("canvas packed")
        self.firstFrame = Frame(self.canvas)
        #totalFrame + label
        totalInfoF = Frame(self.firstFrame)
        totalInfoF.grid(row = 0, column = 0, columnspan = 6)
        self.projectInfoF = Frame(self.firstFrame,bd= 3,bg="black")
        self.projectInfoF.grid(row = 1, column = 0, columnspan = 6)
        self.c_frame = self.canvas.create_window((0,0), window=self.firstFrame, anchor = NW)
        
 
        #totalInfoF.bind("<Configure>", self.OnFrameConfigureTwo)
        #self.canvas.bind('<Configure>', self.FrameWidthTwo)
        scroll = Scrollbar(self.canvas, orient = "vertical", 
            command = self.canvas.yview)
        scroll.pack(side = RIGHT, fill = Y)
        self.canvas.config(yscrollcommand = scroll.set)
        #end of scrollbar

 #      self.totApps = SQL query to get the application total
 #      self.totApps = SQL query to get total of accepted applications 
        totAppLab = Label(totalInfoF, text="applications in total, accepted  applications")
        totAppLab.grid(row =0, column = 0) 

        #projectInfo Frame
        #self.projectInfoF = Frame(self.applicationReportWin,bd= 3,bg="black")
        #self.projectInfoF.grid(row = 1, column = 0, columnspan = 6)

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
        buttonFrame = Frame(self.firstFrame)
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
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql = "SELECT Catname from Category"
        self.cursor.execute(sql)
        self.categories=self.cursor.fetchall()
        self.catlist3=[]
        for tup in self.categories:
            self.catlist3.append(tup[0])
        self.cursor.close()
        db.commit()
        db.close()
        
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
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        cursor = db.cursor()
        sql = "SELECT DesigName from Desig"
        cursor.execute(sql)
        self.designation=cursor.fetchall()
        self.deslist=[]
        for tup in self.designation:
            self.deslist.append(tup[0])
        cursor.close()
        db.commit()
        db.close()
        #USE SQL to call list of des names called self.deslist
        #self.deslist=["Add des1 here"," Add des2 here", "No Requirement"]
        self.ProjPageDesdrop=OptionMenu(projInfoFrame2,self.ProjPageDes,*self.deslist)
        self.ProjPageDesdrop.grid(row=0,column=1)
        
        # EWstimated NUmber of Students
        self.estNumStud = IntVar()
        estNumEnt = Entry(projInfoFrame2, width =30, textvariable = self.estNumStud)
        estNumEnt.grid(row=1, column=1)
        #MAJOR
        self.ProjPageMaj=StringVar()
        self.ProjPageMaj.set("Please Select")
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql = "SELECT Mname from Major"
        self.cursor.execute(sql)
        self.majors=self.cursor.fetchall()
        self.majlist=[]
        for tup in self.majors:
            self.majlist.append(tup[0])
        self.cursor.close()
        db.commit()
        db.close()
        self.majlist.append("No Requirement")
        #USE SQL to call list of major names called self.majlist
        #self.majlist=["Add maj1 here"," Add maj2 here", "No Requirement"]
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
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql = "SELECT Dname from Department"
        self.cursor.execute(sql)
        self.departments=self.cursor.fetchall()
        self.deptlist=[]
        for tup in self.departments:
            self.deptlist.append(tup[0])
        self.cursor.close()
        db.commit()
        db.close()
        self.deptlist.append("No Requirement")
        #USE SQL to call list of dept names called self.deptlist
        #self.deptlist=["Add dept1 here"," Add dept2 here", "No Requirement"]
        self.ProjPageDeptdrop=OptionMenu(projInfoFrame2,self.ProjPageDept,*self.deptlist)
        self.ProjPageDeptdrop.grid(row=4,column=1)


        backButton = Button(self.addProjectWin, text = "Back",width = 15, command = self.ApBack)
        backButton.grid(row = 10,column = 0 ,  sticky = E)
        
        submitButton = Button(self.addProjectWin, text = "Submit",width = 15, command =self.submitNewProject)
        submitButton.grid(row = 10,column = 1,  sticky = E)
        self.APAClist =[]

    def submitNewProject(self):
        #need to pput all of this in a try an except
        if len(self.projName.get())==0 or len(self.advisor.get())==0 or len(self.advisorEm.get())==0 or len(self.descript.get())==0 or len(self.ProjPageDes.get())==0:
            return messagebox.showerror("OOps!","Please fill in all fields")
        if self.estNumStud.get()==0:
            return messagebox.showerror("OOps!","Estimated Number of Students cannot be 0")
        if self.ProjPageMaj.get() == "Please Select" or self.ProjPageYr.get() == "Please Select" or self.ProjPageDept.get() == "Please Select":
            return messagebox.showerror("OOps!","Please fill in all fields")
        if not self.APAClist and self.ProjPageCat.get() == "Please Select":
            return messagebox.showerror("OOps!","Please fill in all fields")
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql = "INSERT into Project (Pname, Num_Students, Aname, Aemail, Description, DesigName) VALUES(%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,(self.projName.get(), self.estNumStud.get(), self.advisor.get(), self.advisorEm.get(), self.descript.get(), self.ProjPageDes.get()))
        #print("here we are")
        self.cursor.close()
        db.commit()
        db.close()
        print("project added")
        #Categories
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        if len(self.APAClist) >=1:
            self.APAClist.append(self.ProjPageCat1.get())
        elif not self.APAClist:
            self.APAClist.append(self.ProjPageCat.get())
        self.FinalApAClist=[]
        #print(self.APAClist)
        for item in self.APAClist:
            if item != "Please Select":
                if item not in self.FinalApAClist:
                    self.FinalApAClist.append(item)
        print(self.FinalApAClist)
        for n in self.FinalApAClist:
            sql = "INSERT into Proj_Cat(Pname, Catname) VALUES(%s,%s)"
            self.cursor.execute(sql,(self.projName.get(), n))
        self.cursor.close()
        db.commit()
        db.close()
        print("proj cat added")
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        if self.ProjPageMaj.get() != "No Requirement":
            sql = "INSERT into Requires(Pname, Requirement) VALUES(%s,%s)"
            self.cursor.execute(sql,(self.projName.get(), self.ProjPageMaj.get()))
        self.cursor.close()
        db.commit()
        db.close()
        print("requires added")
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        if self.ProjPageYr.get() != "No Requirement":
            sql = "INSERT into Requires(Pname, Requirement) VALUES(%s,%s)"
            self.cursor.execute(sql,(self.projName.get(), self.ProjPageYr.get()))
        self.cursor.close()
        db.commit()
        db.close()
        print("proj cat added")
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        if self.ProjPageDept.get() != "No Requirement":
            sql = "INSERT into Requires(Pname, Requirement) VALUES(%s,%s)"
            self.cursor.execute(sql,(self.projName.get(), self.ProjPageDept.get()))
        self.cursor.close()
        db.commit()
        db.close()
        self.addProjectWin.withdraw()
        self.ChooseFunc()
    def CreateProjAddCat(self):
        #print("adding a cat for adding a project")
        if self.ProjPageCat.get() == "Please Select":
            return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")

        if self.ApAcRow == 4 : #first run around
            self.APAClist.append(self.ProjPageCat.get())
            self.ProjPageCatdrop.config(state="disabled")

        if self.ApAcRow > 4:
            
            if self.ProjPageCat1.get() == "Please Select":
 #               self.ApAcRow  = self.ApAcRow  - 1
                return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")

            if self.ProjPageCat1.get() not in self.APAClist :
                self.APAClist.append(self.ProjPageCat1.get())
                self.ProjPageCatdrop1.config(state="disabled")

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

        self.numofstuds = IntVar()
        self.estNumStudentsEnt =Entry(self.courseInfoFrame, width =30, textvariable = self.numofstuds)
        self.estNumStudentsEnt.grid(row=5, column =1)

        self.AddCourseCat = StringVar()
        self.AddCourseCat.set("Please Select")
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql = "SELECT Catname from Category"
        self.cursor.execute(sql)
        self.categories=self.cursor.fetchall()
        self.catlist1 =[]
        for tup in self.categories:
            self.catlist1.append(tup[0])
        self.cursor.close()
        db.commit()
        db.close()
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
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql = "SELECT DesigName from Desig"
        self.cursor.execute(sql)
        self.designation=self.cursor.fetchall()
        deslist=[]
        for tup in self.designation:
            deslist.append(tup[0])
        self.cursor.close()
        db.commit()
        db.close()
        #self.deslist=["Add des1 here"," Add des2 here"]
        self.addCourseDesdrop=OptionMenu(self.courseInfoFrame,self.AACDes,*deslist)
        self.addCourseDesdrop.grid(row=3,column=1)

        #Put Buttons in Frame
        self.buttonFrame = Frame(self.addCourseWin)
        self.buttonFrame.grid(row = 1, column = 0, columnspan = 6)

        backButton = Button(self.buttonFrame, text = "Back",width = 15, command = self.Back_Add_course)
        backButton.grid(row = 0,column = 0 ,  sticky = E)
        
        submitButton = Button(self.buttonFrame, text = "Accept",width = 15, command =self.submitNewCourse)
        submitButton.grid(row = 0,column = 1,  sticky = E)

        self.totalAClist=[]
        #self.totalAClist.append(self.AddCourseCat.get())

    def submitNewCourse(self):
        if len(self.newCourseNum.get())==0 or len(self.newCourseName.get())==0 or len(self.newInstructor.get())==0:
            return messagebox.showerror("OOps!","Please fill in all fields")
        if self.numofstuds.get()==0:
            return messagebox.showerror("OOps!","Estimated Number of Students cannot be 0")
        if self.AACDes.get()=="Please Select":
            return messagebox.showerror("OOps!","Please fill in all fields")
        if not self.totalAClist and self.AddCourseCat.get() == "Please Select":
            return messagebox.showerror("OOps!","Please fill in all fields")
        self.FinalCClist=[]
        print(self.totalAClist)
        if not self.totalAClist:
            self.totalAClist.append(self.AddCourseCat.get())
        elif len(self.totalAClist) >=1:
            self.totalAClist.append(self.AddCourseCat1.get())
        
        for item in self.totalAClist:
            if item != "Please Select":
                if item not in self.FinalCClist:
                    self.FinalCClist.append(item)
        print(self.FinalCClist)
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        sql = "INSERT into Course(Cnum, Cname, Instructor, CnumStud, DesigName) VALUES(%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (self.newCourseNum.get(), self.newCourseName.get(), self.newInstructor.get(), self.numofstuds.get(), self.AACDes.get()))
        self.cursor.close()
        db.commit()
        db.close()
        db = pymysql.connect(host="academic-mysql.cc.gatech.edu", db="cs4400_Team_64", user="cs4400_Team_64", passwd="yghz7eph")
        self.cursor = db.cursor()
        for i in self.FinalCClist:
            sql = "INSERT into Course_Cat(Catname, Cnum)VALUES(%s, %s)"
            self.cursor.execute(sql, (i, self.newCourseNum.get()))
                                
        self.cursor.close()
        db.commit()
        db.close()
        self.addCourseWin.withdraw()
        self.ChooseFunc()
        
        
    def Add_Course_Cat(self):
        #print("Adding Course")

        if self.AddCourseCat.get() == "Please Select":
            return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")
        
        if self.ACrow == 4 : #first run around
            self.totalAClist.append(self.AddCourseCat.get())
            self.AddCC.config(state="disabled")

 #       self.ACrow=self.ACrow+1
     

        if self.ACrow > 4: 
            if self.AddCourseCat1.get() == "Please Select":
 #               self.ACrow = self.ACrow - 1
                return messagebox.showerror("OOps!","Please Pick A category before trying to add a new one")
            
            if self.AddCourseCat1.get() not in self.totalAClist :
                self.totalAClist.append(self.AddCourseCat1.get())
                self.AddCC1.config(state="disabled")

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

        #if self.ACrow ==4: #first time around
#            self.estNumStudents1 = IntVar()
#            self.estNumStudents1.set(self.numofstuds.get())
#            var = self.estNumStudents1.get()
#        else:


        var = self.numofstuds.get()
        self.numofstuds= IntVar()
        self.numofstuds.set(var)
            
            

        self.estNumStudentsEnt.destroy()
        
        self.estNumStudentsEnt =Entry(self.courseInfoFrame, width =30, textvariable = self.numofstuds) #estNumStudents1)
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
#Next two for scroll bar
    def FrameWidth(self, event):
        canvas_width = event.width
        self.Main_pageWin2.itemconfig(self.canvas_frame, width = canvas_width)
    def OnFrameConfigure(self, event):
        self.Main_pageWin2.configure(scrollregion=self.Main_pageWin2.bbox("all"))
    def FrameWidthTwo(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.c_frame, width = canvas_width)
    def OnFrameConfigureTwo(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    

win = Tk()
app = CS4400(win)
win.mainloop()

