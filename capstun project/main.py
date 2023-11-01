from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

try:
    data=pandas.read_csv("Unknown.csv")
    if data == None:
        raise ValueError()

except ValueError:
    data=pandas.read_csv("french_words.csv")

dictionary = data.to_dict(orient="records")

random_word = {}

def next_card():
    global random_word
    try:
        random_word = choice(dictionary)
    except IndexError:
        canvas.itemconfig(card_bg,image = back_image)
        canvas.itemconfig(card_title,text="")
        canvas.itemconfig(card_word ,text="You have learned all the french words\nCongragulations!!")
    else:
        canvas.itemconfig(card_bg,image = back_image)
        canvas.itemconfig(card_title,text="French")
        canvas.itemconfig(card_word ,text=random_word["French"])
        window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_bg,image = front_image)
    canvas.itemconfig(card_title,text ="English")
    canvas.itemconfig(card_word ,text=random_word["English"],font=("Ariel",60,"italic"))
    
def known():
    dictionary.remove(random_word)
    data = pandas.DataFrame(dictionary)
    data.to_csv("Unknown.csv",index=False)
    next_card()





#----------------------------------- UI SCREEN -----------------------------------#
#screen
window = Tk()
window.title("Flashy")
window.config(padx = 50,pady = 50,background=BACKGROUND_COLOR)
window.after(3000,func=flip_card)


#canvas
back_image = PhotoImage(file="card_back.png")
front_image = PhotoImage(file="card_front.png")


canvas=Canvas(width = 800,height =526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_bg = canvas.create_image((400,263),image=back_image)
card_title = canvas.create_text((400,150),font=("Ariel",40,"italic"),text="Title")
card_word = canvas.create_text((400,263),font=("Ariel",60,"bold"),text="Word")
canvas.grid(column=0,row=0,columnspan=3)



#button 
right_image = PhotoImage(file="right.png")
rightbutton = Button(image=right_image,highlightthickness=0,command = known)
rightbutton.config(bg=BACKGROUND_COLOR)
rightbutton.grid(column=2,row=1)

wrong_image = PhotoImage(file="wrong.png")
wrongbutton = Button(image=wrong_image,highlightthickness=0,command = next_card)

wrongbutton.config(highlightbackground=BACKGROUND_COLOR)
wrongbutton.grid(column=0,row=1)
 
next_card()
window.mainloop()