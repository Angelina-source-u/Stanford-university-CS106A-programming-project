"""
File: StepUp.py
Name: 陳禹彤 Angelina Chen
------------------------
This program demonstrates how Karel picks up a beeper
at Street 1 Avenue 2 and moves it to Street 2 Avenue 4.

By guiding Karel step by step, we will practice writing
clear and well-structured commands. At the end of the
program, Karel will be facing East at Street 2 Avenue 5.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will be facing East at Street
    2 Avenue 5 at the end of this program.
    """
    move()
    pick_beeper()
    move()
    turn_left()
    move_3times()
    make_a_circle()
    turn_right()
    move_2times()
    turn_left()
    move_2times()
    turn_left()
    move_2times()
    turn_left()
    for i in range(4):
        move()
    turn_right()
    move()
    turn_right()
    for i in range(4):
        move()
    turn_left()
    put_beeper()
    put_6beepers()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_2times():
    move()
    move()
def move_3times():
    move()
    move()
    move()
def put_6beepers():
    for i in range(6):
        put_beeper()
def make_a_circle():
    turn_left()
    move_2times()
    turn_right()
    move_2times()
    turn_right()
    move_2times()
    turn_right()
    move_2times()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)





