import turtle as t

t.shape("classic")
t.speed('fastest')

def draw_levy(L, N):
    """ Рекурсивная функция по рисованию кривой Леви, где L - длинна
        прямой, а N - глубина рекурсии (количество итераций)
    """
    if N == 0:
        t.forward(L)
    else:
        t.left(45)
        draw_levy((L ** 2 / 2) ** 0.5, N - 1)
        t.right(90)
        draw_levy((L ** 2 / 2) ** 0.5, N - 1)
        t.left(45)

draw_levy(100, 10)
