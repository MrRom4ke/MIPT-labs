import turtle as t
t.shape('turtle')
t.speed(3)

for x in range (3):
    t.circle(x*0+40)
    t.circle(x*0-40)
    t.left(x*0+60)
        
t.exitonclick()
