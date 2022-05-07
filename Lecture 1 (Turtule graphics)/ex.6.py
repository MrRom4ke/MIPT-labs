import turtle as t
t.shape('turtle')

for a in range (0, 360, 30):
    t.seth(a)
    t.forward(100)
    t.stamp()
    t.seth(360)
    t.home()

t.exitonclick()
