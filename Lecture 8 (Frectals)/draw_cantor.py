import turtle as t

t.shape("classic")
t.speed(1)

way=400    
def draw_kantors(l,n,x=0,y=0):    
    dist=l/3
    if n == 0:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.forward(l)
        return

    elif n >= 1:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.forward(l)
        draw_kantors(dist,n-1,x,y-20)
        draw_kantors(dist,n-1,x+dist*2,y-20)
        
draw_kantors(way,4,x=-way/2)


