def turn_right():
    turn_left()
    turn_left()
    turn_left()


def pass_the_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    pass_the_hurdle()
