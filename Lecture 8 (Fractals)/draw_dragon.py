import turtle as t

t.shape("classic")
t.speed(1)

def draw_dragon(L, N):
    """ Рекурсивная функция по рисованию кривой Дракона, где L - длинна
        прямой, а N - глубина рекурсии (количество итераций)
    """
    t.forward(L)
    FX(L, N - 1)

def FX(L, N):
    if N == 0:
        return
    FX(L, N - 1)
    t.right(90)
    FY(L, N - 1)
    t.forward(L)
    t.right(90)    
    
def FY(L, N):
    if N == 0:
        return
    t.left(90)
    t.forward(L)
    FX(L, N - 1)
    t.left(90)
    FY(L, N - 1)
    
draw_dragon(50, 4)


