import turtle as t
t.shape('turtle')

n = int(t.textinput(u'Сообщение', 'Введите количество вершин: '))
t.left(180)
while True:
    t.forward(200)
    t.left(180-(180/n))
    if abs(t.pos()) < 1:
        break

t.exitonclick()

