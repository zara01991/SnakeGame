from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
race_is_on = True
score = Score()
123
while race_is_on:
    screen.update()
    time.sleep(0.15)
    #hit_tail = False
    #i = 2

    P = []
    for i in snake.segment[2:]:
        position = (round(i.xcor()),round(i.ycor()))
        P.append(position)
    head_position = (round(snake.head.xcor()), round(snake.head.ycor()))
    #print(P)
    #print(head_position)
    if snake.head.xcor() >= 295 or snake.head.xcor() <= -295 or snake.head.ycor() >= 295 or snake.head.ycor() <= -295 or head_position in P:
        race_is_on = False
        score.home()
        score.game_over()


        # while hit_tail == False and i < len(snake.segment):
        #     if snake.head.xcor() == snake.segment[i].xcor() and snake.head.ycor() == snake.segment[i].ycor():
        #         hit_tail = True
        #         race_is_on = False
        #
        #     else:
        #         i += 1
    else:
        snake.move()
        if snake.head.distance(food) < 15:
            score.add_score()
            food.clear()
            snake.add_tail()
            food = Food()







screen.exitonclick ()