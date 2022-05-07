#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_9_3():
    x = 1
    while not wall_is_on_the_right():
        x += 1
        move_right()
    def tr_verh():
        y = x
        while y != 1:
            for i in range (y - 2):
                move_left()
                fill_cell()
            y -= 2
            move_down()
            if y != 1:
                move_right(y - 1)
    tr_verh()
    def tr_pravo():
        y = x
        for i in range (y // 2):
                move_right()
                move_down()
        while y != 1:
            for i in range (y - 2):
                move_up()
                fill_cell()
            y -= 2
            move_left()
            if y != 1:
                move_down(y - 1)
    tr_pravo()
    def tr_niz():
        y = x
        for i in range (y // 2):
                move_down()
                move_left()
        while y != 1:
            for i in range (y - 2):
                move_right()
                fill_cell()
            y -= 2
            move_up()
            if y != 1:
                move_left(y - 1)
    tr_niz()
    def tr_levo():
        y = x
        for i in range (y // 2):
                move_left()
                move_up()
        while y != 1:
            for i in range (y - 2):
                move_down()
                fill_cell()
            y -= 2
            move_right()
            if y != 1:
                move_up(y - 1)
    tr_levo()
    while not wall_is_on_the_right() and not wall_is_beneath():
        move_down()
        move_left()

if __name__ == '__main__':
    run_tasks()
