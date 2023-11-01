from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():



    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title(string="Quizller")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        
        self.lable = Label(text="SCORE:0",font=("Ariel",14,"italic"),background=THEME_COLOR,fg="white")
        self.lable.grid(column=2,row=0)

        self.canvas = Canvas(width=300,height=250,highlightthickness=0,background="white")
        self.question_text = self.canvas.create_text((150,125),text="puneeth",fill=THEME_COLOR,font=("Ariel",20,"italic"),)
        self.canvas.grid(column=0,row=1,columnspan=3,padx=20,pady=20)
        

        imagef = PhotoImage(file="false.png")
        self.falsebutton = Button(image=imagef,highlightthickness=0,command=self.flase_pressed)
        self.falsebutton.grid(column=0,row=2)
        
        imaget = PhotoImage(file="true.png")
        self.truebutton = Button(image=imaget,highlightthickness=0,command=self.true_pressed)
        self.truebutton.grid(column=2,row=2)


        self.get_next_question()

        self.window.mainloop()
    

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question
            self.canvas.itemconfig(self.question_text,text = q_text)
            self.quiz.check_answer()
        else:
            self.canvas.itemconfig(self.question_text,text="the game has ennde!!")
            self.falsebutton.config(state="disabled")
            self.truebutton.config(state="disabled")
          
    def true_pressed(self):
        self.feedback(self.quiz.check_answer(user_answer="True"))
        


    def flase_pressed(self):
        self.feedback(self.quiz.check_answer(user_answer="False"))

    def feedback(self,answer):
        if answer:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000,func=self.get_next_question)
