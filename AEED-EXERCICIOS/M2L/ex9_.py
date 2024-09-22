'''
9. Do fragmento de código abaixo, determine a complexidade:
'''
for i in range(n):
    for j in range(n):
        mat[i][j] = 0
        for k in range(n):
            mat[i][j] += A[i][k] * B[k][j]

#Pior caso: O(n³) (pois o número total de operações é cúbico em relação ao tamanho de n).
#Melhor caso: O(n³) (a complexidade é a mesma independentemente das condições específicas do problema, 
# porque todos os laços são sempre executados completamente).
