from turtle import Turtle, Screen
import random

def draw_dash_line(timmy:Turtle):
    for i in range(11):
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()
        timmy.forward(5)
def draw_rect(timmy:Turtle):
    #정가각형
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)
def draw_gon(timmy:Turtle):
    for i in range(3,10):
        print(i)
        for _ in range(i):
            timmy.forward(100)
            theta = (i-2)*180/i
            timmy.right(180-theta)
def get_random_color():
    return (random.random(), random.random(), random.random())
def random_walk(timmy:Turtle):
    timmy.pensize(5)
    directions = [90, 180, 0, 270]
    timmy.speed("fastest")
    for i in range(200):
        timmy.pencolor(get_random_color())
        timmy.setheading(random.choice(directions))
        timmy.forward(10)
def spiro_graph(timmy:Turtle):
    timmy.speed("fastest")
    steps = 200
    theta = 360/steps
    for i in range(steps):
        timmy.pencolor(get_random_color())
        timmy.setheading(timmy.heading()+theta)
        timmy.circle(50)

def hirst_painting(timmy:Turtle, screen_height:int, screen_width:int):
    grb_list = [(247, 243, 234), (241, 152, 69), (139, 49, 104), (164, 168, 38), (242, 80, 57), (218, 236, 231), (249, 224, 229), (4, 142, 54), (240, 102, 161), (239, 65, 139)]
    timmy.speed("fastest")
    size_scale = 1.5
    start_w = -screen_width/size_scale
    end_w = screen_width/size_scale
    start_h = -screen_height/size_scale
    end_h = screen_height/size_scale
    batch_size = 30
    dot_list = []
    for i in range(0,batch_size):
        for j in range(0, batch_size):
            p = (start_w+i*(end_w-start_w)/(batch_size-1), start_h+j*(end_h-start_h)/(batch_size-1))
            dot_list.append(p)

    for spot in dot_list:
        timmy.penup()
        timmy.goto(spot)
        timmy.dot(10, random.choice(grb_list))

    

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)
hirst_painting(timmy,screen.canvheight,screen.canvwidth)
#spiro_graph(timmy)
#random_walk(timmy)
#draw_gon(timmy)
#draw_rect(timmy)
#draw_dash_line(timmy)



screen.exitonclick()
