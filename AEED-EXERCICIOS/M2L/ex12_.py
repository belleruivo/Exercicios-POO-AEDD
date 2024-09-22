'''
12. Calcule a complexidade, no pior e no melhor caso, dos fragmentos de código abaixo:
'''

for i=0 to n-1:
    print(i) # executa n vezes, ou seja, linear, O(n) para ambos os casos de pior e melhor caso

for i in range(0,n,2): # começa em 0, vai até n-1, mas só pares, de 2 em 2, ex.: n = 10, imprime 0, 2, 4, 6, 8
    print(i) # executa n/2 vezes, ou seja, linear, O(n) para ambos os casos de pior e melhor caso

for i in range(0,n,2):
    print(i)
    i -= 1
