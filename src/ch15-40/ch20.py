from turtle import Turtle, Screen
from ch20_package.snake import Snake
from ch20_package.food import Food
from ch20_package.scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.update()

screen.listen()
screen.onkey(snake.head_down,"Down")
screen.onkey(snake.head_left,"Left")
screen.onkey(snake.head_right,"Right")
screen.onkey(snake.head_up,"Up")
screen.onkey(snake.add_body,"space")

is_game_on = True
while is_game_on:
    snake.go_forward()
    screen.update()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_body()
        scoreboard.increase_score()
    
    if (snake.head.xcor() > 230 or 
        snake.head.ycor() > 230 or 
        snake.head.xcor() < -230 or
        snake.head.ycor() < -230):
        scoreboard.game_over()
        is_game_on = False

    time.sleep(0.1)

    
    
screen.mainloop()

# snake.del_snake()

# while True:
#     snake.go_forward()

#screen.exitonclick()



