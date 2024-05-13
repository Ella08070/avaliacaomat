def colecao4(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return colecao4(n // 2)
    elif n % 3 == 0:
        return colecao4(n // 3)
    else:
        return False

# Testa números
numero = [6, 9, 16, 21, 26, 54, 72, 218]
for n in numero:
    if colecao4(n):
        print(f"O número {n} pertence a M.")
    else:
        print(f"O número {n} não pertence a M.")
