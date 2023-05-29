from turtle import Turtle, Screen

tim = Turtle()

#etchescetch
def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_counter_clockwise():
    tim.circle(25, 20)
def move_clockwise():
    tim.circle(-25, 20)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
