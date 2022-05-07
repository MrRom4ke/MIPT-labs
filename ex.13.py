import turtle as t
t.shape('turtle')
t.speed(3)

t.color("black")
t.pu()
t.goto(50, 50)
t.pd()
t.left(90)
t.fillcolor("yellow")
t.begin_fill()
t.circle(80)
t.end_fill()

t.pu()
t.goto(-50, 90)
t.pd()
t.fillcolor("blue")
t.begin_fill()
t.circle(10)
t.end_fill()

t.pu()
t.goto(10, 90)
t.pd()
t.fillcolor("blue")
t.begin_fill()
t.circle(10)
t.end_fill()

t.pu()
t.goto(-27, 60)
t.pd()
t.width(10)
t.color("black")
t.left(180)
t.forward(20)

t.pu()
t.goto(10, 30)
t.pd()
t.width(10)
t.color("red")
t.circle(-40, 180)



t.exitonclick()
