from tkinter import *
import sqlite3
from tkinter import messagebox
root=Tk()
root.title("Python Quiz Game!")


##################### Declaring Input Variables ###################
player_name=StringVar()
player_regno=StringVar()
player_section=StringVar()
game_level=IntVar()
Glevel=IntVar()
Name=StringVar()
###################### Getting Player Details #####################
def enter_details():
    global Name
    Name=player_name.get()
    RegNo=player_regno.get()
    Section=player_section.get()
    global GLevel
    GLevel=game_level.get()
    conn=sqlite3.connect("player_details.db")
    #conn.execute("create table player_detail(player_name varchar(10),player_regno text,player_section text,game_level text);")
    conn.execute("insert into player_detail(player_name,player_regno,player_section,game_level)values(?,?,?,?)",(Name,RegNo,Section,GLevel))
    welcome_message='Welcome to the game '+Name+'.\n  Click OK to proceed.'
    messagebox.showinfo('Welcome!',welcome_message)
    conn.commit()
    conn.close()
    root.destroy()
    



#################### Front GUI  Details ###########################
Label(root,text='\n\n\nWelcome!, Welcome to the Python Quiz Game. Enter the details to get started.').pack()
Label(root,text='Name').place(x=200,y=100)
Entry(root,textvar=player_name).place(x=310,y=100)
Label(root,text='Registration No.').place(x=200,y=150)
Entry(root,textvar=player_regno).place(x=310,y=150)
Label(root,text='Section').place(x=200,y=200)
Entry(root,textvar=player_section).place(x=310,y=200)
Label(root,text='Game Level').place(x=200,y=250)
Radiobutton(text='Easy',variable=game_level,value=0).place(x=310,y=250)
Radiobutton(text='Medium',variable=game_level,value=1).place(x=310,y=270)
Radiobutton(text='Hard',variable=game_level,value=2).place(x=310,y=290)
Button(root,text='Submit',command=enter_details).place(x=310,y=330)
root.geometry("700x400")
root.mainloop()

