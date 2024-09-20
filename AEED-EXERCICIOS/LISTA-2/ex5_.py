'''
5. Dada a função abaixo, determine a complexidade:
'''

def tem_duplicacao(lista, n):
    for i in range(n):
        valor = lista[i]
        for j in range(i+1, n):
            if lista[j] == valor:
                return True
    return False
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 8]
n = len(lista)

print(tem_duplicacao(lista, n)) #True

#Pior caso: O(n²) (quando não há duplicatas, e todos os elementos precisam ser comparados).
#Melhor caso: O(1) (se uma duplicação for encontrada imediatamente).
