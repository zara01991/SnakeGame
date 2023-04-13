from turtle import Turtle

class Score(Turtle):
    def __init__(self,score_no, high_score_no):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write("score is: ",False, align="center", font = ('Arial', 15, 'normal'))
        self.goto(120,280)
        self.write("highest score: ",False, align="center", font = ('Arial', 15, 'normal'))
        self.s = score_no
        self.h = high_score_no
        # self.goto(50, 280)
        # self.write(self.s,False, align ="center", font = ('Arial', 15, 'normal') )
        # self.goto(170, 280)
        # self.write(self.h,False, align ="center", font = ('Arial', 15, 'normal') )

    def add_score(self):

        # self.clear()
        #self.s += 1
        self.goto(50, 280)
        self.write(self.s, False, align="center", font=('Arial', 15, 'normal'))
        self.goto(170, 280)
        self.write(self.h, False, align="center", font=('Arial', 15, 'normal'))
        # self.goto(170, 280)
        # self.write(self.h, False, align="center", font=('Arial', 15, 'normal'))

    # def game_over(self):
    #     self.write("GAME OVER", False, align="center", font=('Arial', 25, 'bold'))


    def highest_score(self):
        self.goto(150, 280)
        # if self.s > self.h:
        #     self.write(self.s, False, align="center", font=('Arial', 15, 'normal'))

        # else:
        self.write(self.h, False, align="center", font=('Arial', 15, 'normal'))
