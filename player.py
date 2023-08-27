from turtle import Turtle
INITIAL_POSITION_1=[(-490,-40),(-490,-20),(-490,0),(-490,20),(-490,40)]
INITIAL_POSITION_2=[(490,-40),(490,-20),(490,-0),(490,20),(490,40)]
DISTANCE=20
class Player:
    def __init__(self):
        self.paddles=[]
        self.create_player(INITIAL_POSITION_1)
        self.create_player(INITIAL_POSITION_2)
        self.player_1 = self.paddles[0:5]
        self.player_2 = self.paddles[5:10]

    def create_player(self,position):
        for pos in position:
            new_player=Turtle()
            new_player.penup()
            new_player.shape("square")
            new_player.color("white")
            new_player.goto(pos)
            new_player.setheading(270)
            self.paddles.append(new_player)


    def move_player(self,player):
        if player[0].heading()==270:
            for segment_number in range(len(player)-1,0,-1):
                player[segment_number].goto(player[segment_number-1].pos())
            if player[0].ycor() >= -280:
                player[0].fd(DISTANCE)
            else:
                player[0].goto(player[0].xcor(), -300)
                player[1].goto(player[1].xcor(), -280)
                player[2].goto(player[2].xcor(), -260)
                player[3].goto(player[3].xcor(), -240)
                player[4].goto(player[4].xcor(), -220)
        elif player[-1].heading()==90:
            for segment_number in range(0,len(player)-1,1):
                player[segment_number].goto(player[segment_number+1].pos())
            if  player[-1].ycor() < 280:
                player[-1].fd(DISTANCE)

            else:
                player[-1].goto(player[-1].xcor(), 300)
                player[-2].goto(player[-2].xcor(), 280)
                player[-3].goto(player[-3].xcor(), 260)
                player[-4].goto(player[-4].xcor(), 240)
                player[-5].goto(player[-5].xcor(), 220)


    def up(self,player):
        for i in player:
            i.setheading(90)


    def down(self,player):
        for i in player:
            i.setheading(270)

    def loses(self,ball):
        if ball.xcor()>500:
            return False
        elif ball.xcor()<-500:
            return True

    def restart(self):
        for segment in self.paddles:
            segment.goto(1000, 1000)
        self.paddles.clear()
        self.create_player(INITIAL_POSITION_1)
        self.create_player(INITIAL_POSITION_2)
        self.player_1 = self.paddles[0:5]
        self.player_2 = self.paddles[5:10]