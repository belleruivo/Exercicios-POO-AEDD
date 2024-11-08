# Faça um programa que cadastre n números em uma fila dinâmica e mais n em uma
# pilha dinâmica. Em seguida, o programa deve mostrar 3 relatórios. O primeiro terá os
# números que estão nas duas estruturas. O segundo terá os que estão apenas na fila e
# o terceiro terá os que estão apenas na pilha.

from fila import Fila
from pilha import Pilha 

def obter_numeros(quantidade):
    numeros = []
    for i in range(quantidade):
        while True:
            try:
                numero = int(input(f"Digite o número {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, insira um número válido.")
    return numeros


def relatorios(fila, pilha):
    na_fila = set(fila.elementos())
    na_pilha = set(pilha.elementos())
    
    comum = na_fila.intersection(na_pilha)
    apenas_fila = na_fila - comum
    apenas_pilha = na_pilha - comum

    print("\nRelatório 1: Números que estão nas duas estruturas:")
    print(sorted(comum))

    print("\nRelatório 2: Números que estão apenas na fila:")
    print(sorted(apenas_fila))

    print("\nRelatório 3: Números que estão apenas na pilha:")
    print(sorted(apenas_pilha))


def main():
    n = int(input("Quantos números deseja cadastrar em cada estrutura? "))
    
    fila = Fila()
    pilha = Pilha()
    
    print("\nCadastro na Fila:")
    numeros_fila = obter_numeros(n)
    for num in numeros_fila:
        fila.inserir(num)
    
    print("\nCadastro na Pilha:")
    numeros_pilha = obter_numeros(n)
    for num in numeros_pilha:
        pilha.empilhar(num)
    
    relatorios(fila, pilha)


main()
