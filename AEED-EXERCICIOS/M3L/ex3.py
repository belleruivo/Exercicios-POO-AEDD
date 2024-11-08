# Um vetor de tamanho n, pode conter elementos do alfabeto e numerais 0 a 9. Escreva
# um algoritmo que seja capaz de localizar, pelo método binário, um caractere
# fornecido pelo usuário. Se esse caractere for uma letra, o usuário poderá fornecê-la
# para a busca no formato maiúsculo ou minúsculo.

# O algoritmo divide a lista em duas partes, comparando o elemento buscado com o elemento do meio da lista.

print("-"*30)
print("       MÉTODO BINÁRIO")
print("-"*30)

def busca_binaria(vetor, caractere):
    esquerda = 0
    direita = len(vetor) - 1

    while esquerda <= direita:
        pontoMedio = (esquerda + direita) // 2
        if vetor[pontoMedio] == caractere:
            return pontoMedio
        elif vetor[pontoMedio] < caractere:
            esquerda = pontoMedio + 1
        else:
            direita = pontoMedio - 1

    return -1  

def main():
    vetor = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
    vetor.sort()  

    caractere = input("Digite um caractere (letra ou número): ").strip()

    indice = busca_binaria(vetor, caractere)

    if indice != -1:
        print(f"O caractere '{caractere}' foi encontrado no índice {indice}.")
    else:
        print(f"O caractere '{caractere}' não foi encontrado no vetor.")

main()

