"""
File: Steeplechase.py
Name: 陳禹彤 Angelina Chen
---------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

def jump():
    up()
    move()
    turn_right()
    down()

def turn_right():
    for i in range(3):
        turn_left()

def up():
    while not front_is_clear():
        # east
        turn_left()
        move()
    # north
    turn_right()
    # pre:east, Karel is on the lower left
    # post:north, Karel is on the upper right
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()

    """
    def up():
    #pre:east, Karel is on the lower left
    # post:north, Karel is on the upper right
        turn_left()
        while not right_is_clear():
            move()
        turn_right()
        move()
        turn_right()
    """

def down():
    #pre:facing east, Karel is on the upper right
    #post:facing south, Karel is on the lower right
    while front_is_clear():
        move()
    turn_left()
    """
    move()
    while not right_is_clear():
        #south
        move()
        if not front_is_clear():
            turn_left()
    """


"""
def jump():
    if front_is_clear():
        move()
    if not right_is_clear():
        turn_left()
        for i in range(5):
            move()
    else:
        turn_right()
        move()
        turn_right()
        if not left_is_clear():
            for i in range(5):
                move()

"""







# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
