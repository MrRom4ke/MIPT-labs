import turtle as t
t.shape('turtle')
t.speed(3)

t.left(90)
for n in range (40, 140, 10):
    t.circle(n)
    t.circle(-n)
        
t.exitonclick()
