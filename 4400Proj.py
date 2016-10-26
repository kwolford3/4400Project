from tkinter import *
import pymysql
import os
from re import findall

class CS4400:

    def __init__(self,win):
        print("ran?")
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
        print("Logged in")
        print(username)
        print(password)

    def Register(self):
        print("Registered")
        

win = Tk()
app = CS4400(win)
win.mainloop()
