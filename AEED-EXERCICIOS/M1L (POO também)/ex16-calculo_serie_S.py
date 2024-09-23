'''
16. Sendo S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ... + 1/N, construa um programa que leia N, calcule e mostre o valor da série S.
'''

def calcular_serie(N):
    S = 0.0
    for i in range(1, N + 1):
        if i % 2 == 0:
            S -= 1 / i
        else:
            S += 1 / i
    return S

def ler_valor_N():
    while True:
        try:
            N = int(input("Digite o valor de N (positivo): "))
            if N <= 0:
                print("Por favor, insira um número inteiro positivo.")
            elif N > 100000000:
                print("Por favor, insira um número inteiro positivo menor que 100000000.")
            else:
                return N
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

def main():
    print("------------------------------------------------------------------------------------------------")
    print("Olá, seja bem-vindo(a) ao programa que calcula o valor da série S!")
    print("------------------------------------------------------------------------------------------------")

    N = ler_valor_N()
    valor_serie = calcular_serie(N)
    print(f"O valor da série S é: {valor_serie}")

if __name__ == "__main__":
    main()