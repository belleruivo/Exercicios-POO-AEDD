'''
13. Calcule a complexidade, no pior caso, do fragmento de código abaixo:
'''
for i in range(0, n, 2): #n/2
    for j in range(n, -1, -1):  #n+1 
        if V[i] < V[j]:
            print(i)

#O(n/2*(n+1)) =O(n^2)