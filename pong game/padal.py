from turtle import Turtle,Screen


class Padal(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.shape("square")
        self.shapesize(8,2)
        self.penup()
       
    
    def stepup(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)

    def stepdown(self):
        y=self.ycor()-20
        self.goto(self.xcor(),y)
