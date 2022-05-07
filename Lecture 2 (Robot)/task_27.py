#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    x = 0
    y = x
    while not wall_is_on_the_right():
        if x < y:
            x += 1
            move_right()
        else:
            x = 0
            y += 1
            move_right()
            if not wall_is_on_the_right():
                fill_cell()
        
if __name__ == '__main__':
    run_tasks()
