from turtle import Turtle, Screen
from Item import Paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.tracer(0)
screen.bgcolor("black")

paddle = Paddle()
screen.onkey(paddle.set_left,"Left")
screen.onkey(paddle.set_right,"Right")
screen.update()
screen.listen()

while True:
    #paddle.move_paddle()
    screen.update()



screen.exitonclick()