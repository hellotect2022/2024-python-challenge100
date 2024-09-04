from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 228)
        self.level = 1
        self.score = 0
        self.write(f"Score: {self.score}",align="center",font=("Arial",14,"normal"))
        #self.update_scoreboard()
    
    def increase_score(self):
        self.level += 1
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",14,"normal"))

    def game_over(self):
        self.clear()
        self.write(f"Game Over!!",align="center",font=("Arial",14,"normal"))


