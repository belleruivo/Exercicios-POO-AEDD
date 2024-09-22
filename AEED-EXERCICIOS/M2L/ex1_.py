'''
1. Uma pesquisa sequencial de uma lista ordenada pode ser interrompida quando o alvo
é menor que determinado elemento na lista. Defina uma versão modificada desse
algoritmo e indique a complexidade computacional, usando a notação big-O, do
desempenho nos casos melhor, pior e médio.
'''

def pesquisa_lista(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return f"O número {alvo} está na posição {i}"  
        if lista[i] > alvo:
            break  
    return "Número não encotrado."

lista = [1, 2, 4, 5, 6, 7]
alvo = 4

print(pesquisa_lista(lista, alvo))

#Melhor caso: O(1) (quando o alvo está na primeira posição).
#Pior caso: O(n) (quando o alvo está na última posição ou não está presente).
#Caso médio: O(n) (em média, o elemento é encontrado após percorrer metade da lista).