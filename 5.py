def colecao5(n):
    if n == 'a' or n == 'b':
        return True
    elif n[0] == 'a':
        return colecao5(n[1:])
    elif n[0] == 'b':
        return colecao5(n[1:])
    else:
        return False

# Testa cadeias
cadeias = ['a', 'ab', 'aba', 'aaab', 'bbbbb']
for n in cadeias:
    if colecao5(n):
        print(f'A cadeia "{n}" pertence a S.')
    else:
        print(f'A cadeia "{n}" não pertence a S.')
