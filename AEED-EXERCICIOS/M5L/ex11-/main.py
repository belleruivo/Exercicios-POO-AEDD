'''
Faça um programa que cadastre em uma pilha vários números. A entrada deles será  finalizada com a digitação de um número menor ou igual a zero. Posteriormente, o programa deve gerar duas filas: a primeira com os números pares e a segunda, com  os números ímpares. A saída do programa deve apresentar a pilha digitada e as filas geradas. Caso alguma das filas seja vazia, deve-se mostrar a mensagem.
'''

from pilha import Pilha
from separador import SeparadorParImpar

def main():
    pilha = Pilha()
    print("Digite números para empilhar (Digite um número menor ou igual a zero para finalizar):")
    while True:
        numero = int(input("Número: "))
        if numero <= 0:
            break
        pilha.push(numero)

    # Criar uma cópia para exibir a pilha original antes de esvaziá-la
    pilha_original = pilha.stack.copy()

    # Separar os números usando a classe SeparadorParImpar
    separador = SeparadorParImpar(pilha)
    separador.separar()
    fila_pares = separador.get_fila_pares()
    fila_impares = separador.get_fila_impares()

    # Saída dos resultados
    print("\nPilha digitada:")
    print(" -> ".join(map(str, pilha_original)) if pilha_original else "Pilha vazia")

    print("\nFila de números pares:")
    print(fila_pares if not fila_pares.is_empty() else "Fila vazia")

    print("\nFila de números ímpares:")
    print(fila_impares if not fila_impares.is_empty() else "Fila vazia")

if __name__ == "__main__":
    main()
