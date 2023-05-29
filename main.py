import turtle
from turtle import Turtle, Screen
import random
# tim = Turtle()
#
# #etchescetch
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def move_counter_clockwise():
#     tim.circle(25, 20)
# def move_clockwise():
#     tim.circle(-25, 20)
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen = Screen()
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_counter_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear_screen)
# screen.exitonclick()

#

# turtle race

colors = ["red", "orange", "yellow", "green", "blue"]
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
all_turtles = []
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race?")
print(user_bet)
height = -100
for tutle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle", )
    new_turtle.color(colors[tutle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=height)
    height += 30
    all_turtles.append(new_turtle)
user_bet = True
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"your won, the winning turtle was {winning_color}")
            else:
                print(f"Sorry your lost, the winner was {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()