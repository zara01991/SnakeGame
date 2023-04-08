from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")

segments = []
screen.tracer(0)
# create snake body

for i in range(0,3):
    turtle = Turtle(shape = "square")
    turtle.speed("fastest")
    turtle.color("white")
    turtle.penup()

    turtle.goto(0-i*20,0)
    segments.append(turtle)
# move the snake
#screen.update()
game_on = True

while game_on:
    screen.update()
    time.sleep(1)
    for i in range(0,3):
        t = segments[-i-1]
        t.speed("slowest")
        t.penup()

        # if t.xcor() > 280:
        #     game_on = False
        if i < 2:
            t.goto(segments[-i - 2].xcor(), segments[-i - 2].ycor())
        else:
            t.forward(20)


        #t.forward(10)









screen.exitonclick ()