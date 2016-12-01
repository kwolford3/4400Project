from tkinter import *

class CS4400:
#Login Page done
    def __init__(self,win):
        self.loginWin = win
        self.loginWin.title("Login")
        self.canvas = Canvas(self.loginWin, bg = 'pink')
        self.canvas.pack(side = RIGHT, fill = BOTH, expand = True)
        self.CPframe=Frame(self.canvas,bd= 3,bg="black")
        self.canvas_frame = self.canvas.create_window((0,0),
            window=self.CPframe, anchor = NW)
        mail_scroll = Scrollbar(self.canvas, orient = "vertical", 
            command = self.canvas.yview)
        mail_scroll.pack(side = RIGHT, fill = Y)
        self.canvas.config(yscrollcommand = mail_scroll.set)
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
        self.CPframe.bind("<Configure>", self.OnFrameConfigure)
        self.canvas.bind('<Configure>', self.FrameWidth)

    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
win = Tk()
app = CS4400(win)
win.mainloop()
