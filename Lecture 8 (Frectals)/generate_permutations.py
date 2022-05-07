def find(number, A):
    """ ищет number в A и возвращает  True, если такой есть
        False, если такого нет
    """
    for x in A:
        if number == x:
            return True
    return False

def generate_premutations(N:int, M:int=-1, prefix=None):
    """ Генерация перестановок N чисел в M позициях,
        с префиксом prefix
    """
    M = N if M == -1 else M # По умолчанию N чисел в N позициях
    prefix = prefix  or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_premutations(N, M-1, prefix)
        prefix.pop()

generate_premutations(4)
