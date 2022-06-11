from turtle import Turtle

#Create scoreboard
class Scoreboard(Turtle):
    def __init__(self):

        super(Scoreboard, self).__init__()
        self.score=0
        with open ("scoreboard.txt","r") as result:
            self.highscore=int(result.read())
        self.penup()
        self.hideturtle()
        self.goto(920, 50)
        self.color('Green')
        self.write(f'Score: {self.score}\nHigh Score: {self.highscore}',align="center",font=('Arial',28,'normal'))

#updating scoreboard
    def update_scoreboard(self):
        self.clear()
        if self.score>self.highscore:
            self.highscore=self.score
            with open("scoreboard.txt","w") as result:
                result.write(f"{self.highscore}")
        self.write(f'Score: {self.score} High Score: {self.highscore}',align="center",font=('Arial',16,'normal'))

#reset scoreboard after exit game
    def reset(self):
        self.score=0
        self.update_scoreboard()

    def add_point_to_score(self):
        self.score+=1
        self.update_scoreboard()