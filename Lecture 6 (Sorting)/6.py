def insert_sort(A):
    """ Сортировка списка А методом вставки
    """
    pass

def choise_sort(A):
    """ Сортировка списка А методом выбора
    """
    pass

def bubble_sort(A):
    """ Сортировка списка А методом пузырька
    """
    pass

def test_sort(sort_algorithm):
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4 ,5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted elsa "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted elsa "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 3]
    A_sorted = [1, 2, 3, 4 ,5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted elsa "Fail")
