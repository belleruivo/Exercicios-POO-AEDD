'''
Escreva um algoritmo que receba valores em um vetor e imprima “ORDENADO” se o
vetor estiver em ordem crescente. Qual é a complexidade deste seu algoritmo?
'''

def verificar_ordenacao(vetor):
    # Loop para verificar se os elementos estão em ordem crescente
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:  # Se um elemento for maior que o próximo
            print("NÃO ORDENADO")  # Imprime se não estiver ordenado
            return  # Sai da função

    print("ORDENADO")  # Se não encontrou nenhum desvio, imprime que está ordenado

# Exemplo de uso
vetor = [1, 2, 3, 4, 5]  # Insira os valores do vetor aqui
verificar_ordenacao(vetor)
