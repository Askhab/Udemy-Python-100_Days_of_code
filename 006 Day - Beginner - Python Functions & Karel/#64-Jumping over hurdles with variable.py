def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pass_the_hurdle():
    turn_left()
    while not right_is_clear() and wall_on_right():
        move()
    else:
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        else:
            turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        pass_the_hurdle()
