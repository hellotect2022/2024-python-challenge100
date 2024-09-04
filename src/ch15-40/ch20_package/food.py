from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.penup()
        self.setposition(0, 100)

    def get_pos(self):
        return self.pos()

    def refresh(self):
        self.setposition(random.randint(-200,200), random.randint(-200,200))