import turtle as t

t.shape("classic")
t.speed('fastest')

def draw_minkowski(L, N):
    """ Рекурсивная функция по рисованию кривой Минковского, где L - длинна
        прямой, а N - глубина рекурсии (количество итераций)
    """
    if N == 0:
        t.forward(L)
    else:
        draw_minkowski(L, N - 1)
        t.left(90)
        draw_minkowski(L, N - 1)
        t.right(90)
        draw_minkowski(L, N - 1)
        t.right(90)
        draw_minkowski(L, N - 1)
        draw_minkowski(L, N - 1)
        t.left(90)
        draw_minkowski(L, N - 1)
        t.left(90)
        draw_minkowski(L, N - 1)
        t.right(90)
        draw_minkowski(L, N - 1)

draw_minkowski(5, 3)
