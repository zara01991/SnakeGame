from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write("score is: ",False, align="center", font = ('Arial', 15, 'normal'))
        self.s = 0
        self.goto(50, 280)
        self.write(self.s,False, align ="center", font = ('Arial', 15, 'normal') )

    def add_score(self):
        self.undo()
        self.s += 1
        self.write(self.s, False, align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.write("GAME OVER", False, align="center", font=('Arial', 25, 'bold'))