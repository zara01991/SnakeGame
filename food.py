from turtle import Turtle, Screen
import random

#screen = Screen()
#
class Food (Turtle):
    def __init__(self):
        super().__init__()
        #food = Turtle()
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.pencolor("blue")
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.dot(10)
        #self.xis = self.xcor()
        #self.yis = self.ycor()


#screen.exitonclick()
