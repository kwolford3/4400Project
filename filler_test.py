from tkinter import *

class CS4400:
#Login Page done
    def __init__(self,win):
        self.Main_pageWin = Toplevel()
        self.Main_pageWin.title("Main Page")
        self.CPframe=Frame(self.Main_pageWin,bd= 3,bg="black")
        self.CPframe.grid(row=6, column=0,columnspan= 5)
        MPCPlab1= Label(self.CPframe, text ="Name", width=70,bg="Light Blue")
        MPCPlab1.grid(row=0,column=0,sticky=W,padx=3,pady=1)
        MPCPlab2= Label(self.CPframe, text ="Type",width=20,bg="Light Blue")
        MPCPlab2.grid(row=0,column=1,sticky=W,pady=1)
        self.canvas = Canvas(self.CPframe)
        self.scrollbar = Scrollbar(self.CPframe, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config( command = self.canvas.yview )
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)
        CPframeCounter=1
        for n in range(100):
            Name=n
            typ=n
            pair= (Name,typ)
            self.SelectBut=Button(self.CPframe, text =str(Name), width=70 ,command = lambda pair= pair: self.view(pair))
            self.SelectBut.grid(row=CPframeCounter,column=0,sticky=W,padx=3,pady=1)
            self.lab=Label(self.CPframe, text =str(typ), width=20)
            self.lab.grid(row=CPframeCounter,column=1,sticky=W,pady=1)
            CPframeCounter=CPframeCounter+1
    

win = Tk()
app = CS4400(win)
win.mainloop()
