'''
31. A multiplicação entre dois números inteiros pode ser definida como uma repetição da
adição de um deles. Exemplo: 3x4 = 4 + 4 + 4
Escreva uma função que multiplique dois números inteiros utilizando esse método. A
seguir, escreva um programa que peça ao usuário um número inteiro e imprima a
tabuada para aquele número (de 1 à 10) utilizando a função construída.
'''

def multiplica(a, b):
    if a == 0 or b == 0:
        return 0
    
    resultado = 0
    for _ in range(abs(b)):
        resultado += abs(a)
    
    # Ajustar o sinal do resultado
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        resultado = -resultado
    
    return resultado

def imprime_tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {multiplica(n, i)}")

def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro entre 1 e 10: "))
            if numero < 1 or numero > 10:
                print("Número inválido. Por favor, digite um número inteiro entre 1 e 10.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    imprime_tabuada(numero)

if __name__ == "__main__":
    main()