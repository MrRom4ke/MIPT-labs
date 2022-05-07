import turtle as t
t.shape('turtle')

for i in range (0, 40, 1):
    x = 5 * i
    t.forward(x)
    t.left(90)

t.exitonclick()
