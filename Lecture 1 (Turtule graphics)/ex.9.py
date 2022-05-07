import turtle as t
import math as m
t.shape('turtle')
t.speed(2)

R = 15 #Радиус первой описаной окружности

def mnugol(n, L):
    q = 360 / n
    while n > 0:
        t.left(q)
        t.forward(L)
        n -= 1

for n in range(3, 13, 1):
    L = 2 * R * m.sin(m.pi / n)
    t.left((180 - 360/ n) / 2)
    mnugol(n, L)
    t.seth(0)
    t.up()
    t.forward(10)                  #Расстояние между окружностями
    t.down()
    R += 10
    
    
t.exitonclick()
