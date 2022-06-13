import turtle
from turtle import Turtle

class Title(Turtle):
    def __init__(self):
        super(Title, self).__init__()
        self.penup()
        self.hideturtle()
        self.color('Red')
        self.setposition(-920, 50)
        self.write('\n\nEurope\nCountry\nGuess Game',align='center',font=('Arial',28,'normal'))