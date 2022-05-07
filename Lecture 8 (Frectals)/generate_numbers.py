def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    #gen_bin(M-1, prefix+"0")
    #gen_bin(M-1, prefix+"1")
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)

def generate_number(N:int, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими незгачищими нулями)
        в N-ричноый системе счисления (N <= 10)
        длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()
    
gen_bin(5) # Только для двоичной системы счисления

generate_number(3, 3) # Для N-ричной системы счисления
