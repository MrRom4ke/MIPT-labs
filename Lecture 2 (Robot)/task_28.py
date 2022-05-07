#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    x = 5
    while x > 0:
        if cell_is_filled():
            x -= 1
            move_right()
        else:
            move_right()
    move_left()
    
if __name__ == '__main__':
    run_tasks()
