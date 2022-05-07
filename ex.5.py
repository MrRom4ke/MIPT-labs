import turtle as t
t.shape('turtle')

for a in range (1, 11, 1):
    t.forward(a*20)
    t.left(90)
    t.forward(a*20)
    t.left(90)
    t.forward(a*20)
    t.left(90)
    t.forward(a*20)
    t.left(90)
    t.pu()
    t.goto(-10*a, -10*a)
    t.pd()

t.exitonclick()
