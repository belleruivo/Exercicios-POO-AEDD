'''5. Faça um programa que cadastre n números, não permitindo números repetidos.
Ordene-os e, em seguida, verifique se o número digitado pelo usuário está no vetor.
Caso encontre, verifique se está numa posição par ou ímpar do vetor:
a. Usando busca sequencial.
b. Usando busca binária.'''

def busca_sequencial(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def busca_binaria(valor, lista):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def main():
    numeros = []
    while True:
        try:
            n = int(input("Quantos números deseja inserir?: "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido\n")
    for c in range(n):
        while True:
            try:
                num = int(input("Insira um número desejado: "))
                if num not in numeros:
                    numeros.append(num)
                    break
                else:
                    print("Número já cadastrado. Tente novamente!\n")
            except ValueError:
                print("Por favor, insira um número inteiro válido\n")

    numeros_ordenados = sorted(numeros)
    print(f"Números cadastrados e ordenados: {numeros_ordenados}\n")

    valor = int(input("Insira um número para verificar: "))
    
    pos_sequencial = busca_sequencial(valor, numeros_ordenados)
    if pos_sequencial != -1:
        print(f"Busca Sequencial: O número {valor} foi encontrado na posição {pos_sequencial}.")
        if pos_sequencial % 2 == 0:
            print("A posição é par.\n")
        else:
            print("A posição é ímpar.\n")
    else:
        print("Busca Sequencial: Número não encontrado.")

    pos_binaria = busca_binaria(valor, numeros_ordenados)
    if pos_binaria != -1:
        print(f"Busca Binária: O número {valor} foi encontrado na posição {pos_binaria}.")
        if pos_binaria % 2 == 0:
            print("A posição é par.\n")
        else:
            print("A posição é ímpar.\n")
    else:
        print("Busca Binária: Número não encontrado.")

main()




