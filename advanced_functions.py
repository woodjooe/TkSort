from dependencies import *

def Donate(C):
    global d
    d="Thank you for !!!!... 0 DT!"
    homeScreen();

def addList(entryAdd):
    global l
    x=int(entryAdd.get())
    l.append(x);
    entryAdd.delete(0, END)


def rmList(entryRm):
    global l
    i=int(entryRm.get())
    l.pop(i-1);
    seeList()


def seeList():
    global l
    global s
    s=str()
    for x in l:
        s+=(str(x)+",");
    sortScreen();

def undoList():
    global l
    l.pop();
    seeList()

def Sort_small_To_big():
    global l
    C=True
    while(C):
        C=False
        for x in range(len(l)-1):
            if(l[x]>l[x+1]):
                a=l[x]
                l[x]=l[x+1]
                l[x+1]=a
                C=True
    seeList()

def Sort_big_To_small():
    global l
    C=True
    while(C):
        C=False
        for x in range(len(l)-1):
            if(l[x]<l[x+1]):
                a=l[x]
                l[x]=l[x+1]
                l[x+1]=a
                C=True
    seeList()

def homeScreen():

    clear_frame()
    global d

    window.update_idletasks()
    posB=(bellButtonPosition[0]*((window.winfo_width())/1024),
    bellButtonPosition[1]*(window.winfo_height()/600))

    posC=(computerButtonPosition[0]*(window.winfo_width()/1024),
    computerButtonPosition[1]*(window.winfo_height()/600))

    posH=(hammerButtonPosition[0]*(window.winfo_width()/1024),
    hammerButtonPosition[1]*(window.winfo_height()/600))

    posG=(giftButtonPosition[0]*(window.winfo_width()/1024),
    giftButtonPosition[1]*(window.winfo_height()/600))

    C = Canvas(frame,bd=2,bg=backgroundColor,confine=True,height=500,width=1000)

    coord=(200,100,100,200)

    window.iconphoto(True,icon);
    C.create_image(posB[0],posB[1],image=Bell)
    C.create_image(posC[0],posC[1],image=Computer)
    C.create_image(posH[0],posH[1],image=Hammer)
    C.create_image(posG[0],posG[1],image=Gift)
    C.create_text(300, 50, text=d, fill="purple", font=('Helvetica 15 bold'))

    #BUTTONS AND CONFIGS
    bellButton=Button(frame, text="Exit", command=Exit,
     width=190, height=15,
      image=butt,
     fg='purple',
     compound='center',
     )

    giftButton=Button(frame, text="Donate", command=lambda:Donate(C),
     width=190, height=15,
     image=butt,
      fg='purple',
      compound='center',
     )

    hammerButton=Button(frame, text="Sort", command=sortScreen,
     width=190, height=15,
      image=butt,
       fg='purple',
       compound='center',
     )
    computerButton=Button(frame, text="Settings", command=settingsScreen,
     width=190, height=15,
      image=butt,
       fg='purple',
       compound='center',
     )

    bellButton.place(x=posB[0]-30,y=posB[1]-15)

    hammerButton.place(x=posH[0]-30,y=posH[1]-15)

    computerButton.place(x=posC[0]-30,y=posC[1]-15)

    giftButton.place(x=posG[0]-30,y=posG[1]-15)
    C.pack()
    frame.pack()



def changeSize(x,y,a,b):
    changeSize0(x,y,a,b)
    settingsScreen()


def settingsScreen():

    window.update_idletasks()
    clear_frame()

    posB=(bellButtonPosition[0]*((window.winfo_width())/1024),
    bellButtonPosition[1]*(window.winfo_height()/600))

    posC=(computerButtonPosition[0]*(window.winfo_width()/1024),
    computerButtonPosition[1]*(window.winfo_height()/600))

    posH=(hammerButtonPosition[0]*(window.winfo_width()/1024),
    hammerButtonPosition[1]*(window.winfo_height()/600))

    posG=(giftButtonPosition[0]*(window.winfo_width()/1024),
    giftButtonPosition[1]*(window.winfo_height()/600))

    level_1_Resolution=Button(frame,text="720 × 480", command=lambda: changeSize(720,480,300,100))
    level_2_Resolution=Button(frame,text="1024 × 600", command=lambda: changeSize(1024,600,150,50))
    level_3_Resolution=Button(frame,text="1280 × 720", command=lambda: changeSize(1200,720,150,50))

    back=Button(frame,text="Back to Menu",command=homeScreen);

    print(posB[0]-30)
    print(posB[1]-15)



    level_1_Resolution.place(x=posB[0]-30,y=posB[1]-15)
    level_2_Resolution.place(x=posH[0]-30,y=posH[1]-15)
    level_3_Resolution.place(x=posC[0]-30,y=posC[1]-15)
    back.place(x=posG[0]-40,y=posG[1]+30)

def resetSort():
    global l
    l=list();
    global s
    s=str();
    sortScreen();


def sortScreen():

    window.update_idletasks()
    clear_frame()

    posB=(bellButtonPosition[0]*((window.winfo_width())/1024),
    bellButtonPosition[1]*(window.winfo_height()/600))

    posC=(computerButtonPosition[0]*(window.winfo_width()/1024),
    computerButtonPosition[1]*(window.winfo_height()/600))

    posH=(hammerButtonPosition[0]*(window.winfo_width()/1024),
    hammerButtonPosition[1]*(window.winfo_height()/600))

    posG=(giftButtonPosition[0]*(window.winfo_width()/1024),
    giftButtonPosition[1]*(window.winfo_height()/600))

    C = Canvas(frame,bd=2,bg=backgroundColor,confine=True,height=500,width=1000)



    entryAdd=Entry(frame,font=("Arial",10,"bold"))
    entryRm=Entry(frame,font=("Arial",10,"bold"))

    window.bind('<Return>',(lambda event:addList(entryAdd)))

    resetSortButton=Button(frame, text="Reset", command=resetSort,
    width=190, height=15,
    image=butt,
    fg='red',
    compound='center',
    )
    seeListButton=Button(frame, text="See list ", command=seeList,
    width=190, height=15,
    image=butt,
    fg='green',
    compound='center',
    )
    undoListButton=Button(frame, text="Undo ", command=undoList,
    width=190, height=15,
    image=butt,
    fg='green',
    compound='center',
    )
    sortButtonS=Button(frame, text="Sort from small to big", command=Sort_small_To_big,
    width=190, height=15,
    image=butt,
    fg='black',
    compound='center',
    )
    sortButtonB=Button(frame, text="Sort from big to small", command=Sort_big_To_small,
    width=190, height=15,
    image=butt,
    fg='black',
    compound='center',
    )
    addToList=Button(frame, text="add number:", command=lambda:addList(entryAdd),
    width=190, height=15,
    image=butt,
    fg='purple',
    compound='center',
    )
    rmFromList=Button(frame, text="remove number of position:", command=lambda:rmList(entryRm),
    width=190, height=15,
    image=butt,
    fg='purple',
    compound='center',
    )
    back=Button(frame,text="Back to Menu",command=homeScreen,
    width=190, height=15,
    image=butt,
    fg='#333333',
    compound='center',);


    C.create_text(300, 50, text=s, fill="black", font=('Helvetica 15 bold'))
    C.pack()
    entryAdd.place(x=posB[0]+200,y=posB[1]-15,width=100)
    entryRm.place(x=posH[0]+200,y=posH[1]-15,width=100)

    addToList.place(x=posB[0]-30,y=posB[1]-15)
    rmFromList.place(x=posH[0]-30,y=posH[1]-15)
    undoListButton.place(x=posG[0]+250,y=posG[1]-15)
    sortButtonB.place(x=posG[0]-30,y=posG[1]-15)
    sortButtonS.place(x=posG[0]-30,y=posG[1]-50)
    seeListButton.place(x=posG[0]-30,y=posG[1]-85)

    resetSortButton.place(x=posG[0]-310,y=posG[1]-15)
    back.place(x=posG[0]-30,y=posG[1]+20)
