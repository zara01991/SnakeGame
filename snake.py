from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        segments=[]
        for i in range(0, 3):
            turtle = Turtle(shape="square")
            #turtle.speed("fastest")
            turtle.color("white")
            turtle.penup()
            turtle.goto(0 - i * 20, 0)
            segments.append(turtle)
        self.segment = segments
        self.head = segments[0]
        #self.xiss = segments[0].xcor()
        #self.yiss = segments[0].xcor()

    def move_up(self):
        t = self.segment[0]
        if t.heading() == 0:
            t.left(90)
        elif t.heading() == 180:
            t.right(90)

    def move_down(self):
        t = self.segment[0]
        if t.heading() == 0:
            t.right(90)
        elif t.heading() == 180:
            t.left(90)

    def move_left(self):
        t = self.segment[0]
        if t.heading() == 90:
            t.left(90)
        elif t.heading() == 270:
            t.right(90)

    def move_right(self):
        t = self.segment[0]
        if t.heading() == 90:
            t.right(90)
        elif t.heading() == 270:
            t.left(90)



    def move(self):
        screen = Screen()
        for i in range(0, len(self.segment)):
            t = self.segment[-i - 1]
            t.speed("slowest")
            t.penup()

            if i < len(self.segment) - 1:
                t.goto(self.segment[-i - 2].xcor(), self.segment[-i - 2].ycor())
            else:
                screen.listen()
                screen.onkey(key="Up",fun = self.move_up)
                screen.onkey(key="Down", fun=self.move_down)
                screen.onkey(key="Left", fun=self.move_left)
                screen.onkey(key="Right", fun=self.move_right)


                t.forward(20)
                # if t.xcor() > 280:
                #     game_on = False

    def add_tail(self):
        tail = Turtle(shape="square")
        tail.speed("fastest")
        tail.color("white")
        tail.penup()
        tail.goto(self.segment[-1].xcor(),self.segment[-1].ycor())
        self.segment.append(tail)


