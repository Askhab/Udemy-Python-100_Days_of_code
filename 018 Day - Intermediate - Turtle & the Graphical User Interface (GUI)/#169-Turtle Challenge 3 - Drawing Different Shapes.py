import turtle as t

colors = ["purple", "OliveDrab", "MediumTurquoise", "LightSteelBlue", "RoyalBlue", "goldenrod1", "LightSeaGreen"]
tim = t.Turtle()

start_num = 3
for i in range(0, 7):
    angle = 360 / start_num
    tim.color(colors[i])
    for j in range(start_num):
        tim.right(angle)
        tim.forward(100)
    start_num += 1


screen = t.Screen()
screen.exitonclick()
