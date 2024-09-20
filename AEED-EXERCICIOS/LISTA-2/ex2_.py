'''
O método de lista reverse inverte os elementos da lista. Defina uma função chamada
reverse que inverte os elementos no argumento de lista (sem usar o método reverse).
Tente tornar essa função a mais eficiente possível e indique sua complexidade
computacional usando a notação big-O.
'''

def reverse(lista):
    # Obter o tamanho da lista
    n = len(lista)
    # Percorre até a metade da lista e troca os elementos simétricos
    for i in range(n // 2):
        # Trocar o elemento na posição i com o elemento na posição -i-1
        lista[i], lista[n - i - 1] = lista[n - i - 1], lista[i]
    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reverse(lista))