from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.y_code=10
        self.x_code=10

    def move(self):
        x=self.xcor()+self.x_code
        y=self.ycor()+self.y_code
        self.goto(x,y)

    def bounce(self):
        self.y_code *= -1

    def padalhit(self):
        self.x_code *= -1
        