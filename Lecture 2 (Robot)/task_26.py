#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def krest():
        move_down()
        fill_cell()
        move_down()
        move_right()
        fill_cell()
        move_up()
        fill_cell()
        move_right()
        fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_left()
    for x in range (4):
        for y in range(9):
            krest()
            move_right(4)
        krest()
        move_down(4)
        move_left(36)
    for z in range(9):
        krest()
        move_right(4)
    krest()
    move_left(36)

if __name__ == '__main__':
    run_tasks()
