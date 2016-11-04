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
            #self.Choose_functionality()
        #else:
        # self.flag="Student"
        
        print("Logged in")
        print(username)
        print(password)
        self.Main_page() #will need to put under else once sql is added
       

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
        self.registerWin.deiconify()

    def RegisterCheck(self):
        print("Register check")
        username = self.user.get()
        userEmail = self.email.get()
        password =self.passw.get()
        confirmPass = self.conf
        print(username, userEmail, password, confirmPass)
        print("calling main page")
        self.Main_page() #ONLY RUN IF A SUCCESFUL REGISTER
        
    def Main_page(self):
        #called by ME Page
        #also called by a succesfull login page
       
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
        self.MainPageCat.set("Pick a Category")
        #USE SQL to call list of category names called self.catlist
        self.catlist=["Add cat1 here"," Add Cat 2 here"]
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
        self.MainPageDesdrop=OptionMenu(self.Main_pageWin,self.MainPageMaj,*self.majlist)
        self.MainPageDesdrop.grid(row=2,column=1)

        MainPageLabYear = Label(self.Main_pageWin,text="Year:")
        MainPageLabYear.grid(row=3,column=0)
        #print("ran")
        self.MainPageYear=StringVar()
        self.MainPageYear.set("Please Select")
        #USE SQL to call list of Designation names called self.deslist
        self.yearlist=["Freshman","Sophmore","Junior","Senior"]
        self.MainPageDesdrop=OptionMenu(self.Main_pageWin,self.MainPageYear,*self.yearlist)
        self.MainPageDesdrop.grid(row=3,column=1)
        
    def Add_Cat_MainPage(self):
        #print("adding a cat")
        self.MainPageRow = self.MainPageRow +1
        self.MainPagedrop=OptionMenu(self.Main_pageWin,self.MainPageCat,*self.catlist)
        self.MainPagedrop.grid(row=self.MainPageRow,column=3)
        self.AddCatBut =Button(self.Main_pageWin, text="Add a Category", command = self.Add_Cat_MainPage)
        self.AddCatBut.grid(row=self.MainPageRow,column=4)
        
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

    def Choose_functionality(self):
        #called by
        print ("admin choose functionality page")

    def View_apps(self):
        #called by
        print ("admin view apps")

    def Popular_proj(self):
        #called by
        print ("admin popular projects page")

    def App_report(self):
        #called by
        print("admin view application reports")

    def Add_proj(self):
        #called by
        print("admin add project")
        
    def Add_course(self):
        #called by
        print("admin add course")
    

win = Tk()
app = CS4400(win)
win.mainloop()
