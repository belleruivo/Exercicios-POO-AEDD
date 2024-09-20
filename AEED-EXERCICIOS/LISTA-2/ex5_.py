'''
5. Dada a função abaixo, determine a complexidade:
'''

def tem_duplicacao(array, n):
    for i=0 to n-1:
        val = array[i]
        for j=(i+1) to n-1:
            if array[j] == val:
                return true
    return false
    

#Pior caso: O(n²) (quando não há duplicatas, e todos os elementos precisam ser comparados).
#Melhor caso: O(1) (se uma duplicação for encontrada imediatamente).
