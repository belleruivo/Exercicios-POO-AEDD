'''5. Fazer um programa que calcule e escreva o número de grãos de milho que podem ser
colocados em um tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros
seguintes o dobro do quadro anterior. Obs.: esse número cresce muito rápido, tenha
o cuidado de testar se ele não sofre um overflow.'''

n = 1

for c in range(1, 65):

    print(f"Quadro {c}: {n} grãos")
    n = n*2

print(f"Total: {n}")


