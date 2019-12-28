from tkinter import *
from details import *
import sqlite3
from tkinter import messagebox

j=-1




def main():
    app=Application()   #creating object for Application class
    s="Welcome to the Quiz "+Name
    app.master.title(s)
    app.mainloop()

class Application(Frame):

    def __init__(self, master=None):
        #print(GLevel)
        #Calling the constructor when object is created.
        #Variables initialized and set the grid as per need.
        Frame.__init__(self, master)
        self.grid()

        #setting grid

        self.optionA = StringVar() # control variable for option A
        self.optionB = StringVar() # control variable for option B
        self.optionC = StringVar() # control variable for option C
        self.optionD = StringVar() # control variable for option D
        self.selected_answer = StringVar() # variable to get the selected answer
        self.correct_answer = "" # to store the correct answer before randomizing options
        self.question = StringVar() # control variable for the question to be loaded
        self.score = IntVar()# to hold the score
        self.name= StringVar()
        top = self.winfo_toplevel()
        self.createWidgets(top) # call to create the necessary widgets
        self.load_question(top) # load the first question


    def createWidgets(self,top):
	
	#Function that creates all the necessary Tkinter widgets. All the widgets are specified here while creation.
	
	
        top.geometry("800x180")
        top.resizable(True,True)
        top.grid_columnconfigure(0,weight=1)
        top.grid_columnconfigure(9,weight=1)
        top.grid_rowconfigure(0,weight=1)
        top.grid_rowconfigure(9,weight=1)
#	top.configure(background="white")

        self.optionA.set('Hello A!')
        self.optionB.set('Hello B!')
        self.optionC.set('Hello C!')
        self.optionD.set('Hello D!')
        self.question.set('Demo Question')

        #Creating the menu buttons
        self.menu = Menu(self)
        self.menubar = Menu(self.menu, tearoff=0)
        self.menubar.add_command(label="New Game", command=lambda: self.new_game(top))
        self.menubar.add_command(label="About", command=self.about)
        self.menubar.add_command(label="Quit", command=self.confirm_quit)
        self.master.config(menu=self.menubar)

        #Creating the buttons
        self.quitButton = Button(self, text='Quit', command=self.confirm_quit)
        self.nextButton = Button(self, text='Next', command=lambda: self.load_question(top))

	#Creating Radio buttons for options
        self.radioButtonA = Radiobutton(self,anchor='w', 
                            textvariable=self.optionA, 
                            variable = self.selected_answer, 
                            value = 'A',
                            command = lambda: self.set_ans(1)) # the radio button call 'set_ans()' with the number to set the 'selected_answer' variable
        self.radioButtonB = Radiobutton(self,anchor='w',
                            textvariable=self.optionB, 
                            variable = self.selected_answer,
                            value = 'B', 
                            command = lambda: self.set_ans(2))
        self.radioButtonC = Radiobutton(self,anchor='w',
                            textvariable=self.optionC, 
                            variable = self.selected_answer, 
                            value = 'C', 
                            command = lambda: self.set_ans(3))
        self.radioButtonD = Radiobutton(self,anchor='w',
                            textvariable=self.optionD,
                            variable = self.selected_answer,
                            value = 'D', 
                            command = lambda: self.set_ans(4))

            
            #Creating the labels for options and questions
        self.score.set(5)    
        self.label_question = Label(self,textvariable=self.question)
        self.label_score = Label(self,text='Score:')
        self.label_score_value = Label(self,textvariable=self.score,anchor='e')

        
        self.label_question.grid(column=3,row=1,columnspan=4)
        self.label_score.grid(column=7,row=3)
        self.label_score_value.grid(column=8,row=3,sticky=N+S+W+E)
        self.radioButtonA.grid(column=2,row=4,sticky=N+S+W+E)
        self.radioButtonB.grid(column=5,row=4,sticky=N+S+W+E)
        self.radioButtonC.grid(column=2,row=6,sticky=N+S+E+W)
        self.radioButtonD.grid(column=5,row=6,sticky=N+S+E+W)
        self.quitButton.grid(column=5,row=8)
        self.nextButton.grid(column=3,row=8)


    def new_game(self,top):
        a=0
        #When the New Game button from the menu is clicked, the game resets the score to 0 and a new question is loaded.
        global j
        j=0
        self.load_question(top)
        self.score.set(0)


    def about(self):
	
	#Load the About Info Box.
	
        messagebox.showinfo("About Quiz!","Welcome to Quiz!\n This Quiz Game is developed as an project work in which the player can test his/her knowledge based on various concepts in Python Language.")
        

    def confirm_quit(self):
	
	#Function to confirm quit when the player presses Quit Button. If yes, Quit the application, If no, return to the game.
	
        choice = messagebox.askyesno('Quit Application','Are you sure you wish to stop playing! ?')
        if choice == True:
            self.destroy()
            
        else:
            pass


    def set_ans(self,answer):
	
	#Function to set the 'selected_answer' variable to the selected option label to compare with correct answer later.
	#Args: answer - gets the option number which calls this function.
	
        if answer==1:
            self.selected_answer = self.optionA.get()
        elif answer==2:
            self.selected_answer = self.optionB.get()
        elif answer == 3:
            self.selected_answer = self.optionC.get()
        elif answer == 4:
            self.selected_answer = self.optionD.get()


    def validate_ans(self):
	
	#Function to validate the selected answer with the correct answer. If they match, increase the score by 5.
	
        print ("In Validate answer:")
        print ("selected:",self.selected_answer)
        print ("Correct:",self.correct_answer)
        
        if str(self.selected_answer) == str(self.correct_answer):
            self.score.set(self.score.get()+5)
            print ("Selected Answer is Correct!")
        else:
            self.score.set(self.score.get()-5)
            print ("Selected Answer is Incorrect!")


    def load_question(self,top):
        a=0
        self.validate_ans()
        global j

        j=j+1
        if j==10:
            f_score='Your Final Score is:'+str(self.score.get())
            messagebox.showinfo('Congratulations !!',f_score)
            self.destroy()
            return 0
        if j!=11:
            if GLevel==0:
                conn=sqlite3.connect("easy.db")
                c=conn.cursor()
                c.execute('SELECT * FROM easy')
                i=c.fetchall()
            elif GLevel==1:
                conn=sqlite3.connect("medium.db")
                c=conn.cursor()
                c.execute('SELECT * FROM medium')
                i=c.fetchall()
            else:
                conn=sqlite3.connect("hard.db")
                c=conn.cursor()
                c.execute('SELECT * FROM hard')
                i=c.fetchall()
        
            self.question.set(i[j][0]) #taking details of the question from the database
            self.optionA.set(i[j][1]) 
            self.optionB.set(i[j][2])
            self.optionC.set(i[j][3])
            self.optionD.set(i[j][4])
            self.correct_answer=i[j][5]
        
        
        
        
        length=len(self.question.get())  # get the length of the question
        width=str(100+15*length)	
        top.geometry(width+"x220")
        self.radioButtonA.deselect()
        self.radioButtonB.deselect()
        self.radioButtonC.deselect()
        self.radioButtonD.deselect()
        
            


if __name__ =="__main__":
    main()
