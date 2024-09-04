from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270 
LEFT = 180 
RIGHT = 0
INITIAL_POINT = [(0,0),(-MOVE_DISTANCE,0),(-MOVE_DISTANCE*2,0)]


class Snake:

    def __init__(self):
        self.bodies = []
        self.create_snake()

        # set snake head
        self.head = self.bodies[0]
        self.head.color("black")
        self.head.shape("circle")

    def create_snake(self):
         for pos in INITIAL_POINT:
            square = Turtle(shape="square")
            square.penup()
            square.color("green")
            square.goto(pos)
            self.bodies.append(square)

    def go_forward(self):
        for index in range(len(self.bodies)-1,0,-1):
            next_pos = self.bodies[index-1].pos()
            self.bodies[index].setpos(next_pos)
        self.head.forward(MOVE_DISTANCE)

    def add_body(self):
        new_body = Turtle(shape="square")
        new_body.color("green")
        new_body.penup()
        last_body = self.bodies[-1]
        new_body.goto(last_body.xcor(), last_body.ycor())
        self.bodies.append(new_body)

    def head_left(self):
        if self.head.heading != RIGHT:
            self.head.seth(LEFT)
    def head_right(self):
        if self.head.heading != LEFT:
            self.head.seth(RIGHT)
        
    def head_down(self):
        if self.head.heading != UP:
            self.head.seth(DOWN)
    def head_up(self):
        if self.head.heading != DOWN:
            self.head.seth(UP)


            
    

    
