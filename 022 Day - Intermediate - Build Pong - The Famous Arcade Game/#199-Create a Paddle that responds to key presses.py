from turtle import Turtle, Screen

PADDLE_ONE_X_POS = 350
PADDLE_ONE_Y_POS = 0

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Paddles setup
paddle = Turtle("square")
paddle.color("azure")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(PADDLE_ONE_X_POS, PADDLE_ONE_Y_POS)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
