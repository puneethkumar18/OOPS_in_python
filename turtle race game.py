from turtle import Turtle, Screen
import random
screen=Screen()
screen.setup(width=200 , height=200)
screen.textinput(title="what is your bet", prompt="which colour will going to win")
list=[]
y_axis= 250
for i in range(8):
    y_axis-=50
    tim=Turtle(shape="turtle")
    list.append(tim)
    tim.penup()
    tim.goto(-200,y_axis)



def move():
    choice=random.choice(list)
    choice.fd(20)
for i in range(200):
    move()

screen.exitonclick()