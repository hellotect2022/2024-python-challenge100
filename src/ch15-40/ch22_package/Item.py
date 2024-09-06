from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(0, 0)
    
    def set_left(self):
        print("left")
        x = self.xcor() - 20
        self.goto(x, self.ycor())
        

    def set_right(self):
        print("right")
        #self.seth(0)
        x = self.xcor() + 20
        self.goto(x, self.ycor())

    def move_paddle(self):
        x = self.xcor()
        if round(x) < 340 and round(x) > -340:
            self.forward(0.1)
        else:
            self.forward(0)
            print(x,round(x),round(x)<340)