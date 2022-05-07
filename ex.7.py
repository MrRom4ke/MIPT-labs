import turtle as t
t.shape('turtle')

k = 0.1     #смещение точки
fi = 0.1    #радиан
fidegr = fi * (180/3.14) 
for i in range (0, 1000):
    ro = k * fi
    t.forward(ro)
    t.left(fidegr)
    fi += 0.1
    ro += ro

t.exitonclick()
