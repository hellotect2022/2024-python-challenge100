from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Whitch turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
racers = []
def create_turtles():
    y = -90
    for color in colors:
        tim = Turtle(shape="turtle")
        tim.color(color)
        tim.penup()
        tim.goto(-230,y)
        y+=30
        racers.append(tim)

create_turtles()

if user_bet :
    is_race_on = True

while is_race_on:
    for turtle in racers:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
            break

screen.exitonclick()