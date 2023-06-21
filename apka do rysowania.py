import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_backwards():
    tim.backward(20)


def move_forwards():
    tim.forward(20)


def clear():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()