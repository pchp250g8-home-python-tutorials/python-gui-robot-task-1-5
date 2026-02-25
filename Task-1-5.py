from robot import *

move_down()
for i in range(3):
    for j in range(i+3):
        if(i % 2 == 0) and is_free_right():
            paint()
            move_right()
        elif is_free_left():
            paint()
            move_left()
            paint()
    if(is_free_down()):
        move_down()