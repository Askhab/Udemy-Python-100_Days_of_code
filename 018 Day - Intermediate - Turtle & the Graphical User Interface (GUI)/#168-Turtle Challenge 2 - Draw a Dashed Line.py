import turtle as t

tim = t.Turtle()
tim.color("SeaGreen3")
tim.pencolor("purple")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = t.Screen()
screen.exitonclick()
