'''
8. Dada a função abaixo, determine a complexidade:
'''

def ache_min(array, n): #--> O(n)
    min = array[0] #--> O(1)

    for i=0 to n-1: #--> O(n)
        if array[i] < min:
            min = array[i] #--> O(1)
    return min

# geral --> O(n), mas depende do tamanho do array