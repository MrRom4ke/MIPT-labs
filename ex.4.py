import turtle as t
t.shape('turtle')
t.pu()
t.goto(50, 50)
t.pd()
t.left(90)

for a in range (0, 360, 10):
    t.forward(20)
    t.left(10)

t.exitonclick()
