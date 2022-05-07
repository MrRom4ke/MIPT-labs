#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    def zakras_2_diag():
        move_down()
        while not wall_is_beneath():
            move_right()
            fill_cell()
            move_down()
        move_left()
        while not wall_is_on_the_left():
            move_up()
            fill_cell()
            move_left()
    for i in range(6):
        zakras_2_diag()
    move_down()
    move_right()
    fill_cell()
    move_down()


if __name__ == '__main__':
    run_tasks()
