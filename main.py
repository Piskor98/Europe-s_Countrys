
#import modules
import csv
import time
import turtle
from turtle import Turtle

import pandas

from title import Title
from scoreboard import Scoreboard

#screen settings
screen=turtle.Screen()
screen.title("Guess Country Game")
screen.setup(2200,1340,0,0)

#View on game title

#Create basic needed object
game_title=Title()
scoreboard=Scoreboard()

#Add new shape as image
new_turtle_shape="European_countries_by_population(beginning_of_2018).GIF"
turtle.addshape(new_turtle_shape)
turtle.shape(new_turtle_shape)

# for every states on the map - need to get (x,y) positions
# def get_position_on_click(x,y):
#     print(x,y)
# turtle.onscreenclick(get_position_on_click)
# turtle.mainloop()   #function to keeping screen open


state_name=Turtle()
def answer_moving_setup():
    state_name.penup()
    state_name.hideturtle()
    state_name.color('Black')
answer_moving_setup()

game=True

# open data from csv file, read data, save as list
with open("52 Europe Country.csv", "r") as f:
    data = csv.reader(f)
    rows = []
    for row in data:
        rows.append(row)

# main loop
while game:
    #prompt for user
    answer=screen.textinput(title="Please guess the Country name", prompt="What's another Country name?")
    answer=answer.title()

# check that if answer is correct and save score
    for row in rows:
        if row[0] == answer:
            x=row[1]
            y=row[2]
            state_name.setposition(int(x),int(y))
            state_name.write(f'{answer}',align="center",font=('Arial',18,'normal'))
            scoreboard.add_point_to_score()
            rows.remove(row)

        else:
            pass
#Exit app
        if answer=='exit' or answer =='Exit':
            scoreboard.reset()
            missing_country=[country for country in row]
            new_data=pandas.DataFrame(missing_country)
            new_data.to_csv('Country_to_learn.csv')
            screen.bye()


#


#Prompt



