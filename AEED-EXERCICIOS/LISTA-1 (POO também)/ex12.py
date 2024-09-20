'''
Elabore um programa que calcule e mostre o fatorial de um número (N!), sendo que N
é fornecido pelo usuário.
Sabemos que:
N! = 1 x 2 x 3 x 4 x...x (N - 1) x N;
0! = 1, por definição.
'''

def calcular_fatorial(n):
    if n == 0:
        return 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro não-negativo para calcular o fatorial: "))
            if numero < 0:
                print("Número inválido. Por favor, digite um número inteiro não-negativo.")
            else:
                resultado = calcular_fatorial(numero)
                print(f"O fatorial de {numero} é {resultado}.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

main()
