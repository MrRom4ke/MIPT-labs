#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_30():
    flag_found = True
    while flag_found:
        flag_found = False
        while not wall_is_on_the_right():
            move_right()
            while not wall_is_beneath():
                move_down()
                flag_found = True
        while not wall_is_on_the_left():
            move_left()
            while not wall_is_beneath():
                move_down()
                flag_found = True
            
        

if __name__ == '__main__':
    run_tasks()
