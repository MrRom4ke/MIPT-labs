import turtle as t

t.shape("classic")
t.speed('fastest')

def draw_koch(L, N):
    """ Рекурсивная функция по рисованию кривой Коха, где L - длинна
        прямой, а N - глубина рекурсии (количество итераций)
    """
    if N == 0:
        t.forward(L)
    else:
        draw_koch(L / 3, N - 1)
        t.left(60)
        draw_koch(L / 3, N - 1)
        t.right(120)
        draw_koch(L / 3, N - 1)
        t.left(60)
        draw_koch(L / 3, N - 1)

draw_koch(100, 1)
