def A(n):
    if n == 1:
        return 2
    else:
        return A(n - 1) / 2


#Testa pra valor n
for i in range(1, 6):
    print(f"A({i}) = {A(i)}")
