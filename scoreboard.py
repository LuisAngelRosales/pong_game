from turtle import Turtle
LOCATIONS=[(-70,260),(40,260),(-100,0)]
ALIGNMENT="center"
FONT="Courier"
FONT_SIZE=15
class Scoreboard:
    def __init__(self):
        self.texts=[]
        self.create_texts()
        self.score_1=0
        self.score_2=0

    def create_texts(self):
        for i in LOCATIONS:
            self.text=Turtle()
            self.text.penup()
            self.text.pencolor("white")
            self.text.hideturtle()
            self.text.goto(i)
            self.texts.append(self.text)

    def increase_score(self,player1_lose):
        if player1_lose:
            self.score_2+=1
        else:
            self.score_1+=1
    def show_score(self):
        self.texts[0].clear()
        self.texts[1].clear()
        self.texts[0].write(self.score_1,font=(FONT,50))
        self.texts[1].write(self.score_2,font=(FONT,50))

    def point(self):
        self.texts[2].write("GOAL! \nPRESS 'SPACE' to \nCONTINUE",font=(FONT, FONT_SIZE),align=ALIGNMENT)
    def restart(self):
        self.texts[2].clear()

    def player_win(self):
        if self.score_1 ==5:
            self.texts[2].write(f"Player 1 wins! \nPRESS 'SPACE' to \nRESTART", font=(FONT, FONT_SIZE), align=ALIGNMENT)
        elif self.score_2 == 5:
                self.texts[2].write(f"Player 2 wins! \nPRESS 'SPACE' to \nRESTART", font=(FONT, FONT_SIZE),
                                    align=ALIGNMENT)
    def paused(self,paused):
        if paused:
            self.texts[2].write("PAUSE", font=(FONT, FONT_SIZE), align=ALIGNMENT)
        else:
            self.texts[2].clear()