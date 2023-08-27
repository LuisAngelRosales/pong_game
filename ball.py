from turtle import Turtle
import random

ROOF=310
FLOOR=-310
RIGHT=0
RIGHT_UP=45
UP=90
UP_LEFT=135
LEFT=180
LEFT_DOWN=225
DOWN=270
DOWN_RIGHT=315

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.turn(True)
        self.angle=0
        self.speed=10




    def turn(self,player1_loses):
        first_turn=True
        if first_turn:
            first_turn=False
            self.local=random.choice([True,False])
            if self.local:
                self.angle=RIGHT_UP
                self.setheading(self.angle)
            else:
                self.angle = UP_LEFT
                self.setheading(self.angle)
        else:
            if player1_loses:
                self.angle = UP_LEFT
                self.setheading(self.angle)
            else:
                self.angle = RIGHT_UP
                self.setheading(self.angle)

    def bounce_wall(self):
        if self.ycor() >= ROOF:
            if self.heading()<UP and self.heading()>RIGHT:
                self.angle=DOWN_RIGHT
                self.setheading(self.angle)
            elif self.heading()>UP and self.heading()<LEFT:
                self.angle = LEFT_DOWN
                self.setheading(self.angle)
        if self.ycor()<=FLOOR:
            if self.heading()<DOWN and self.heading()>LEFT:

                self.angle=UP_LEFT
                self.setheading(self.angle)
            elif self.heading()>DOWN and self.heading()<360:
                self.angle = RIGHT_UP
                self.setheading(self.angle)

    def bounce_paddle(self,player_1,player_2):
        for i in player_1:

            if self.distance(i) <20:
                if self.heading() > UP and self.heading() < LEFT:
                    self.angle = RIGHT_UP
                    self.setheading(self.angle)
                    self.speed+=1
                elif self.heading()<DOWN and self.heading()>LEFT:
                    self.angle = DOWN_RIGHT
                    self.setheading(self.angle)
                    self.speed += 1
        for i in player_2:
            if self.distance(i) <20:
                if self.heading() < UP and self.heading() > RIGHT:
                    self.angle = UP_LEFT
                    self.setheading(self.angle)
                    self.speed += 1
                elif self.heading()>DOWN and self.heading()<360:
                    self.angle = LEFT_DOWN
                    self.setheading(self.angle)
                    self.speed += 1

    def move(self):
        self.fd(self.speed)

    def goes_away(self):
        if self.xcor()>500 or self.xcor()<-500:
            return True

    def restart(self):
        self.clear()
        self.home()
        self.turn(False)
        self.speed=10
