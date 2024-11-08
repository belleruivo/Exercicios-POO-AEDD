# Implemente uma versão generalizada para busca binária numa matriz m x n.

print("-"*45)
print("        BUSCA BINÁRIA EM UMA MATRIZ")
print("-"*45)
def busca_binaria_linha(linha, caractere):
    esquerda = 0
    direita = len(linha) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if linha[meio] == caractere:
            return meio 
        elif linha[meio] < caractere:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1  

def busca_binaria_matriz(matriz, caractere):
    for i in range(len(matriz)):
        indice = busca_binaria_linha(matriz[i], caractere)
        if indice != -1:
            return (i, indice)  # Retorna a posição (linha, coluna)

    return (-1, -1) 

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    caractere = int(input("Digite um número a ser buscado: "))

    posicao = busca_binaria_matriz(matriz, caractere)

    if posicao != (-1, -1):
        print(f"O número {caractere} foi encontrado na posição {posicao}.")
    else:
        print(f"O número {caractere} não foi encontrado na matriz.")

main()
