from turtle import Screen, Turtle
import time
import keyboard

LINE_SIZE=25
screen= Screen()
screen.tracer(0)
screen.setup(1020,650)
screen.bgcolor("black")
turtle=Turtle()
turtle.hideturtle()
turtle.up()
turtle.goto(0,325)
turtle.setheading(270)
turtle.pensize(5)
turtle.pencolor("white")
line_number=1

for line in range(int(LINE_SIZE/screen.yscale)):
    if line_number%2!=0:
        turtle.down()
        turtle.fd(LINE_SIZE)
        line_number+=1

    else:
        turtle.up()
        turtle.fd(LINE_SIZE)
        line_number += 1


from player import Player
from ball import Ball
from scoreboard import Scoreboard

def continue_game():
    global on_wait
    on_wait = False
    player.restart()
    ball.restart()
    scoreboard.restart()

def restart():
    global on_wait
    on_wait = False
    player.restart()
    ball.restart()
    scoreboard.score_1=0
    scoreboard.score_2=0
    scoreboard.restart()
    scoreboard.show_score()

def toggle_pause():
    global paused
    global  on_wait
    if not on_wait:
        paused = not paused

def turn_off():
    global game_is_on
    game_is_on=not game_is_on
screen.onkeypress(lambda: player.up(player.player_1), "w")
screen.onkeypress(lambda: player.down(player.player_1), "s")
screen.onkeypress(lambda: player.up(player.player_2), "Up")
screen.onkeypress(lambda: player.down(player.player_2), "Down")
screen.onkeypress(turn_off,"Escape")


screen.listen()


player=Player()
screen.update()
ball=Ball()
scoreboard=Scoreboard()
game_is_on=True
paused=False
on_wait=False


while game_is_on:
    if not paused and not on_wait:
        screen.onkeypress(toggle_pause, "space")
        screen.update()
        time.sleep(0.010)
        scoreboard.show_score()
        ball.move()
        ball.bounce_wall()
        ball.bounce_paddle(player.player_1,player.player_2)
        if ball.goes_away():
            on_wait=True
            ball.turn(player.loses(ball))
            scoreboard.increase_score(player.loses(ball))

            if scoreboard.score_1 ==5 or scoreboard.score_2 ==5:
                scoreboard.player_win()
                scoreboard.show_score()
                screen.onkeypress(restart, "space")
            else:
                scoreboard.point()
                screen.onkeypress(continue_game, "space")
                screen.listen()


        if keyboard.is_pressed("w") or keyboard.is_pressed("s"):
            player.move_player(player.player_1)
        if keyboard.is_pressed("Up") or keyboard.is_pressed("Down"):
            player.move_player(player.player_2)



    screen.update()
    screen.delay(100)
    if not on_wait:
        scoreboard.paused(paused)




screen.bye()