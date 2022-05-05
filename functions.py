from setUp import *

def homeScreen(): pass
def settingsScreen():pass

def settingsScreen(): print("WAT")

def changeSize0(x,y,a,b):

    s=str(x)+"x"+str(y)+"+"+str(a)+"+"+str(b);
    window.geometry(s)

    window.resizable(width=False, height=False)



def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

def clear_frame():
    if(frame.winfo_children()):
        for widgets in frame.winfo_children():
            widgets.destroy()

def Donate():
    print("thanks");


def sendFeed_Back():
    print("thanks")

def Exit():
   window.destroy();




def IdleAnimation():
   window.destroy();


#ws.config(background="black")
