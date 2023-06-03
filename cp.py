import tkinter as t
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os

bt=t.Tk()
bt.title("BookTopia")
l1=t.Label(bt,text="WELCOME TO BOOKTOPIA",borderwidth=2,relief="solid",bg="DarkGoldenrod2",fg="DarkOrange4",font=("Felix Titling",60,"bold"))
l2=t.Label(bt,text="READ, WRITE AND TALK ALL ABOUT YOUR FAVOURITE BOOKS!!!",bg="goldenrod2",fg="sienna4",font=("Harrington",25))


# Designing window for registration

def register():
    global reg
    reg = Toplevel(bt)
    reg.title("Register")
    reg.geometry("600x650")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    l1=t.Label(reg, text="Please enter details below", bg="lightblue")#.pack()
    l2=t.Label(reg, text="")#.pack()
    username_lable = t.Label(reg, text="Username * ")
    username_lable.pack()
    username_entry = t.Entry(reg, textvariable=username)
    username_entry.pack()
    password_lable = t.Label(reg, text="Password * ")
    password_lable.pack()
    password_entry = t.Entry(reg, textvariable=password, show='*')
    password_entry.pack()
    l3=t.Label(reg, text="").pack()
    b=t.Button(reg, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
    l1.place(x=80, y=80)
    username_lable.place(x=80, y=160)
    username_entry.place(x=80, y=180)
    password_lable.place(x=80, y=260)
    password_entry.place(x=80, y=280)
    b.place(x=100, y=500)
    def click():
        b.after(1, reg.destroy)
    


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(bt)
    login_screen.title("Login")
    login_screen.geometry("600x650")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    l1=t.Label(login_screen, text="Username * ").pack()
    username_login_entry = t.Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    l2=t.Label(login_screen, text="").pack()
    l3=t.Label(login_screen, text="Password * ").pack()
    password_login_entry = t.Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    l4=t.Label(login_screen, text="").pack()
    b=t.Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    l=t.Label(reg, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("350x300")
    l=t.Label(login_success_screen, text="Login Success").pack()
    b=t.Button(login_success_screen, text="OK", command=delete_login_success).pack()
    
# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("350x300")
    l1=t.Label(password_not_recog_screen, text="Invalid Password ").pack()
    b1=t.Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("350x300")
    l=t.Label(user_not_found_screen, text="User Not Found").pack()
    b=t.Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global ms
    ms = Toplevel(bt)
    ms.geometry("1080x1080")
    ms.title("Account Login")
    l1=t.Label(ms, text="Select Your Choice", bg="lightblue", width="100", height="2", font=("Calibri", 13))#.pack()
    l2=t.Label(ms, text="").pack()
    b1= t.Button(ms, text="Login", height="10", width="30", command = login, bg="lightgreen", fg="black")#.pack()
    Label(text="").pack()
    b2= t.Button(ms, text="Register", height="10", width="30", command=register, bg="lightgreen", fg="black")#.pack()
    l1.place(x=80, y=80)
    #l2.place()
    b1.place(x=280, y=200)
    b2.place(x=600, y=200)

    ms.mainloop()



def clicked():
    r=Toplevel(bt)
    r.title("READING")
    l3=t.Label(r,text="WELCOME TO READSVILLE",borderwidth=2,relief="solid",bg="LightPink2",fg="IndianRed1",font=("COPPERPLATE GOTHIC BOLD",60))
    lband=t.Label(r,text="",bg="LightPink2",width=191,height=3)
    def click():
        but.after(1,r.destroy)
    but=t.Button(r,text="HOMEPAGE",relief=RAISED,command=click,bg="black",fg="red")
    l3.place(x=70,y=80)
    but.place(x=18,y=22)
    lband.place(x=10,y=10)
    r.geometry("2100x2100")
    r.configure(bg="RosyBrown2")
def clicked2():
    f=Toplevel(bt)
    f.title("FANDOM")
    l3=t.Label(f,text="THE KINGDOM OF FANS",borderwidth=2,relief="solid",fg="RoyalBlue3",bg="dark turquoise",font=("COPPERPLATE GOTHIC BOLD",60))
    lband=t.Label(f,text="",bg="dark turquoise",width=191,height=3)
    def click():
        but.after(1,f.destroy)
    but=t.Button(f,text="HOMEPAGE",relief=RAISED,bg="black",fg="blue",command=click)
    l3.place(x=148,y=80)
    but.place(x=18,y=22)
    lband.place(x=10,y=10)
    f.geometry("2080x2080")
    f.configure(bg="LightSkyBlue1")
    
    
    def mycommand():
        h= Toplevel(bt)
        h.title("HARRY POTTER")
        l= t.Label(h, text="Welcome To The Wizarding World of Harry Potter", borderwidth=2, fg="gold",bg="black",font=("TIMES NEW ROMAN",30), height=8)
        l2= t.Label(h, text="Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.\nThe novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry.\nThe main story arc concerns Harry's struggle against Lord Voldemort, a dark wizard who intends to become immortal, \noverthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles")
        def click():
            but.after(1, h.destroy)
        
        l.place(x=450, y=100)
        l2.place(x=100, y=350)
        h.configure(bg="black")
        h.geometry("2080x2080")
    img= PhotoImage(file='/Users/neeleshdharam/Desktop/harrypotter.png')
    img_label= Label(image= img)
    b= Button(f, image= img, command= mycommand)
    b.pack(pady=30)
    text= Label(f, text= "")
    text.pack(pady=30)
    b.place(x=100, y=250)
    f.mainloop()
    def click():
        but.after(1,f.destroy)
    but=t.Button(f,text="HOMEPAGE",relief=RAISED,bg="black",fg="blue",command=click)
    l3.place(x=148,y=80)
    but.place(x=18,y=22)
    lband.place(x=10,y=10)
    f.geometry("2080x2080")
    f.configure(bg="LightSkyBlue1")

    
    
    def mycommand2():
        
        d= Toplevel(bt)
        d.title("DIVERGENT")
        L= t.Label(d, text= "This is the Divergent Trilogy!!", borderwidth=2, fg="blue", bg= "black", font=("TIMES NEW ROMAN", 30), height=8)

        txt=t.Label(d, text="In Beatrice prior’s dystopian Chicago, society is divided into five factions, each medicated to the cultivation of a particular virtue- \nCandor (the honest), Abnegation (the selfless), Dauntless (the brave), Amity (the peaceful), and Erudite (the intelligent).\nOn appointed day of every year, all sixteen-year-olds must select the faction to which they will devote the rest of their lives. \nFor Beatrice, the decision is between staying with her family and being who she really is- she can’t have both. \nSo she makes a choice that surprises everyone, including herself. \nDuring the highly competitive initiation that follows, Beatrice renames herself Tris and struggles to determine who her friends really are—\nand where, exactly, a romance with a sometimes fascinating, sometimes infuriating boy fits into the life she's chosen.\nBut Tris also has a secret, one she's kept hidden from everyone because she's been warned it can mean death.\nAnd as she discovers a growing conflict that threatens to unravel her seemingly perfect society, \nshe also learns that her secret might help her save those she loves . . . or it might destroy her.")
        
        def click():
            but.after(1, d.destroy)
        #l3= t.Label(d,text="THE DIVERGENT SERIES",borderwidth=2,relief="solid",fg="green4",bg="SpringGreen3",font=("COPPERPLATE GOTHIC BOLD",45))
        
        L.place(x=450, y=100)
        txt.place(x=100, y=350)
        d.configure(bg= "blue")
    img= PhotoImage(file='/Users/neeleshdharam/Desktop/divergent1.png')
    img_label= Label(image= img)
    b1= Button(f, image= img, command= mycommand2)
    b1.pack(pady=60)
    text= Label(f, text= "")
    text.pack(pady=60)
    b1.place(x=500, y=250)
    f.mainloop()
    def click():
        but.after(1,f.destroy)
    but=t.Button(f,text="HOMEPAGE",relief=RAISED,bg="black",fg="blue",command=click)
    l3.place(x=148,y=80)
    but.place(x=18,y=22)
    lband.place(x=10,y=10)
    f.geometry("2080x2080")
    f.configure(bg="LightSkyBlue1")

    def mycommand3():
        T= Toplevel(bt)
        T.title("TWILIGHT")
        l= t.Label(T, text="Welcome to the world of Vampires!!", borderwidth=2, fg="black",bg="red", height=8)
        txt=t.Label(T, text="Twilight is a series of vampire novels by Stephenie Meyer.\nIt follows the life of Bella Swan, a teenager who moves to Forks, Washington and finds her life radically changed \n when she falls in love with a vampire named Edward Cullen.")
        txt2=t.Label(T, text="While creating an amazing world of Vampires, \nthe author has also included supernatural species like werewolves and witches that adds on to the excitement!")

        def click():
            but.after(1, T.destroy)
        l.place(x=550, y=100)
        txt.place(x=200, y=300)
        txt2.place(x=200, y=350)
        T.configure(bg="black")

    img= PhotoImage(file='/Users/neeleshdharam/Desktop/twilight.png')
    img_label= Label(image= img)
    b2= Button(f, image= img, command= mycommand3)
    b2.pack(pady=30)
    text= Label(f, text= "")
    text.pack(pady=30)
    b2.place(x=800, y=250)
    f.mainloop()
    def click():
        but.after(1,f.destroy)
    but=t.Button(f,text="HOMEPAGE",relief=RAISED,bg="black",fg="blue",command=click)
    l3.place(x=148,y=80)
    but.place(x=18,y=22)
    lband.place(x=10,y=10)
    f.geometry("2080x2080")
    f.configure(bg="LightSkyBlue1")

    def mycommand4():
        p= Toplevel(bt)
        p.title("PERCY JACKSON")
        l= t.Label(p, text="Welcome to the world of Percy Jackson", fg="gold", font= ("TIMES NEW ROMAN", 30))
        txt= t.Label(p, text="Perseus Jackson is an eighteen-year-old Greek demigod, the son of Poseidon and Sally Jackson.\n He is the main protagonist and narrator of the Percy Jackson and the Olympians series, and one of the main characters of The Heroes of Olympus series. \nHe is the head counselor at Poseidon's Cabin and a former Praetor of the Twelfth Legion at Camp Jupiter, formerly belonging to the legion's Fifth Cohort. \nHe was the temporary host of the Egyptian goddess Nekhbet.") 
        def click():
            but.after(1, p.destroy)
        l.place(x=550, y=100)
        txt.place(x=200, y=350)
        p.configure(bg="black")
    img= PhotoImage(file='/Users/neeleshdharam/Desktop/percy.png')
    img_label= Label(image= img)
    b3= Button(f, image= img, command= mycommand4)
    b3.pack(pady=30)
    text= Label(f, text= "")
    text.pack(pady=30)
    b3.place(x=1200, y=250)
    f.mainloop()
    def click():
        but.after(1,f.destroy)
    but=t.Button(f,text="HOMEPAGE",relief=RAISED,bg="black",fg="blue",command=click)
    l3.place(x=148,y=80)
    but.place(x=18,y=22)
    lband.place(x=10,y=10)
    f.geometry("2080x2080")
    f.configure(bg="LightSkyBlue1")

    
    bu=t.Button(bt,text="HARRY POTTER",cursor="hand2",relief=GROOVE,font=("Book Antiqua",10,"bold"),activebackground="BLACK",width=32,height=10,bg="Salmon",fg="GOLD",command=mycommand)
    bu2=t.Button(bt,text="DIVERGENT",cursor="hand2",relief=GROOVE,font=("Book Antiqua",10,"bold"),width=32,height=10,activebackground="peach puff",bg="Coral",fg="BLUE",command=mycommand2)
    bu3=t.Button(bt,text="TWILIGHT",cursor="hand2",relief=GROOVE,font=("Book Antiqua",10,"bold"),activebackground="peach puff",width=32,height=10,bg="orchid1",fg="RED",command=mycommand3)
    bu4=t.Button(bt, text="PERCY JACKSON", cursor= "hand2", relief= GROOVE,font=("Book Antiqua",10,"bold"),width=32,height=10,activebackground="peach puff",bg="coral",fg="black",command=mycommand4)
   
    bu2.place(x=1050,y=198)
    bu3.place(x=850,y=198)
    bu.place(x=550,y=198)
    bu4.place(x=1400, y=198)
    
    
def clicked3():
    w=Toplevel(bt)
    w.title("WRITING")
    l3=t.Label(w,text="WELCOME TO YOUR WRITING SPACE",borderwidth=2,relief="solid",fg="green4",bg="SpringGreen3",font=("COPPERPLATE GOTHIC BOLD",45))
    lband=t.Label(w,text="",bg="SpringGreen3",width=191,height=3)
    def openFile():
        tf = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/", 
            title="Open Text file", 
            filetypes=(("Text Files", ".txt"),('All files','.*'))
            )
        pathh.insert(END, tf)
        tf = open(tf)
        file_cont = tf.read()
        txtarea.insert(END, file_cont)
       
        tf.close()

    def saveFile():
        tf = filedialog.asksaveasfile(defaultextension='.txt',
                                  filetypes=[("Text file",".txt"),
                                             ("All files",".*")
                                             ])
        data = str(txtarea.get(1.0, END))
        tf.write(data)
        tf.close()


    
    
    # adding frame
    frame = Frame(w)
    frame.place(x=430,y=200)

    # adding scrollbars 
    ver_sb = Scrollbar(frame, orient=VERTICAL )
    ver_sb.pack(side=RIGHT, fill=BOTH)

    hor_sb = Scrollbar(frame, orient=HORIZONTAL)
    hor_sb.pack(side=BOTTOM, fill=BOTH)

    # adding writing space
    txtarea = Text(frame, width=60, height=20)
    txtarea.pack(side=LEFT)

    # binding scrollbar with text area
    txtarea.config(yscrollcommand=ver_sb.set)
    ver_sb.config(command=txtarea.yview)

    txtarea.config(xscrollcommand=hor_sb.set)
    hor_sb.config(command=txtarea.xview)

    # adding path showing box
    pathh = Entry(w,width=200)
    pathh.pack(expand=True)
    pathh.place(x=80,y=570)
   
    # adding buttons 
    Button(
        w, 
        text="Open File", 
        command=openFile
        ).place(x=240,y=610)

    Button(
        w, 
        text="Save File", 
        command=saveFile
        ).place(x=640,y=610)

    Button(
        w, 
        text="Exit", 
        command=lambda:w.destroy()
        ).place(x=1040,y=610)


    def click():
        but.after(1,w.destroy)
    but=t.Button(w,text="HOMEPAGE",relief=RAISED,width=10,height=2,bg="black",fg="green",command=click)
    but2=t.Button(w,text="READING",relief=RAISED,width=10,height=2,bg="black",fg="green",command=clicked)
    l3.place(x=60,y=80)
    but.place(x=18,y=15)
    but2.place(x=180,y=15)
    lband.place(x=10,y=10)
    w.geometry("2080x2080")
    w.configure(bg="PaleGreen1")

def clicked4():
    n= Toplevel(bt)
    n.title("FEEDBACK")
    l3=t.Label(n,text="FEEDBACK",borderwidth=2,relief="solid",fg="lightblue",bg="turquoise",font=("COPPERPLATE GOTHIC BOLD",60))
    lband=t.Label(n,text="",bg="turquoise",width=191,height=3)
    def click():
        but.after(1, n.destroy)
    but= t.Button(n,text="HOMEPAGE", relief=RAISED, width=10, height=2, bg="black", fg="black", command=click)
    but1=t.Button(n,text="excellent", command=click,bg="black",fg="green", font=("TIMES NEW ROMAN", 30))
    but2=t.Button(n,text="satisfactory", command=click,bg="black",fg="blue", font=("TIMES NEW ROMAN", 30))
    but3=t.Button(n,text="needs improvement", command=click,bg="black",fg="red", font=("TIMES NEW ROMAN", 30))
    l3.place(x=548,y=80)
    but.place(x=18, y=15)
    but1.place(x=410,y=298)
    but2.place(x=640, y=298)
    but3.place(x=900, y=298)
    lband.place(x=10,y=10)
    n.geometry("2080x2080")
    n.configure(bg="LightSkyBlue1")
    
    def mycommand():
        text.config(text= "press one of the three buttons!")
    img= PhotoImage(file='/Users/neeleshdharam/Downloads/fd.png')
    img_label= Label(image= img)
    b= Button(n, image= img, command= mycommand)
    b.pack(pady=30)
    text= Label(n, text= "")
    text.pack(pady=30)
    b.place(x=250, y=450)
    n.mainloop()



bu= t.Button(bt,text= "ACCOUNT LOGIN",cursor="hand2",relief=GROOVE,font=("Book Antiqua",10,"bold"),activebackground="peach puff",width=32,height=10,bg="Salmon",fg="black",command=main_account_screen)  
bu1=t.Button(bt,text="READING",cursor="hand2",relief=GROOVE,font=("Book Antiqua",10,"bold"),activebackground="peach puff",width=32,height=10,bg="Salmon",fg="black",command=clicked)
bu2=t.Button(bt,text="FANDOM",cursor="hand2",relief=GROOVE,font=("Book Antiqua",10,"bold"),width=32,height=10,activebackground="peach puff",bg="Coral",fg="black",command=clicked2)
bu3=t.Button(bt,text="WRITING",cursor="hand2",relief=GROOVE,font=("Book Antiqua",10,"bold"),activebackground="peach puff",width=32,height=10,bg="orchid1",fg="black",command=clicked3)
bu4=t.Button(bt, text="FEEDBACK", cursor= "hand2", relief= GROOVE,font=("Book Antiqua",10,"bold"),width=32,height=10,activebackground="peach puff",bg="coral",fg="black",command=clicked4)
l1.place(x=280,y=50)
l2.place(x=280,y=180)
bu.place(x=570,y=530)
bu2.place(x=40,y=300)
bu3.place(x=400,y=300)
bu1.place(x=750,y=300)
bu4.place(x=1098, y=300)
bt.configure(bg="goldenrod2")
bt.geometry("2080x2080")
bt.mainloop()
