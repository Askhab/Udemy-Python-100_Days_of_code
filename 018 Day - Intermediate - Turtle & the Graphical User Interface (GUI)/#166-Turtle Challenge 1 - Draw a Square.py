from turtle import Turtle, Screen

tim = Turtle()
# view
tim.shape("turtle")
tim.color("SeaGreen")
tim.pencolor("RoyalBlue")
# movement
for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
