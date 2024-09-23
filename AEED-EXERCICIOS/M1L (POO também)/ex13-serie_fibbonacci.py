'''
13. A série de Fibbonacci é gerada da seguinte forma: os dois primeiros termos são 1, os
demais são dados pela soma dos dois anteriores. Faça um programa que imprima os
“n” primeiros termos da série, sendo “n” dado pelo usuário.
'''

import sys

# limite de dígitos permitidos para conversão de string
sys.set_int_max_str_digits(10000)

MAX_TERMOS = 100

def ler_numero_termos():
    while True:
        try:
            num_termos = int(input(f"Digite o número de termos (máximo {MAX_TERMOS}): "))
            if num_termos <= 0:
                print("Por favor, insira um número inteiro positivo.")
            elif num_termos > MAX_TERMOS:
                print(f"Por favor, insira um número menor ou igual a {MAX_TERMOS}.")
            else:
                return num_termos
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

def fibonacci(n):
    termos = []
    a, b = 1, 1 # guarda os 2 primeiros elementos da série
    for _ in range(n):
        termos.append(a)
        a, b = b, a + b # atualizando os valores de a e b, indo pro looping até acabar
    return termos

def main():
    print("-"*65)
    print("Olá, seja bem-vindo(a) ao programa que imprime os termos da série de Fibonacci!\nPara começar, digite o número de termos que deseja imprimir:")
    print("-"*65)

    num_termos = ler_numero_termos()
    termos = fibonacci(num_termos)
    print("Os primeiros", num_termos, "termos da série de Fibonacci são:")
    print(termos)

if __name__ == "__main__":
    main()