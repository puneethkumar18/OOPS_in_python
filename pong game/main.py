from turtle import Turtle, Screen
from padal import Padal
from ball import Ball
import time

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0) 
l_padal=Padal().goto(-350,0)
r_padal=Padal().goto(350,0)
ball=Ball()




game_is_on=True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.move()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce() 
        print(ball.distance(l_padal))

    if ball.distance(l_padal) < 20 or ball.distance(r_padal) < 20:
        ball.padalhit()

screen.exitonclick()