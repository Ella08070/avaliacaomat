def colecao6(cadeia):
    if cadeia == 'a' or cadeia == 'b' or cadeia == 'c':
        return True
    elif cadeia[0] == 'a' and cadeia[-1] == 'c' and colecao6(cadeia[1:-1]):
        return True
    else:
        return False

# Testa cadeias
cadeias = ['a(b)c', 'a(a(b)c)c', 'a(abc)c', 'a(a(a(a)c)c)c', 'a(aacc)c']
for letras in cadeias:
    if colecao6(letras):
        print(f'A cadeia "{letras}" pertence a W.')
    else:
        print(f'A cadeia "{letras}" não pertence a W.')
