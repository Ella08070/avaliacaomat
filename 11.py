# Encontra indice do maior item em intervalo lista L
def maior(L, j):
    mainmaior = 0  # Maior item em posição zero
    for i in range(1, j):  # Percorre lista na posição 1 até chegar j - 1
        if L[i] > L[
                mainmaior]:  # Se item posição i maior que o maior item
            mainmaior = i  # Atualiza índice mainmaior item
    return mainmaior


# Troca dois itens de posição na lista L
def switch(L, i, j):
    L[i], L[j] = L[j], L[i]  # Troca itens L,i, j


# Função principal joga algoritmo na seleção recursiva
def Srecursiva(L, j):
    if j == 1:  # Se j =1, fica lista ordenada  retorna
        return L

    # Encontra índice do maior item entre 1 e j
    i = maior(L, j)

    # Troca item posição i com item posição j - 1
    switch(L, i, j - 1)

    # Chama função com o j - 1 para continuar a ordenação
    return Srecursiva(L, j - 1)


# Teste 
lista = [6, 4, 9, 1, 8, 2]
total = Srecursiva(lista, len(lista))
print(total)
