'''
34. Uma equação do segundo grau é escrita

ax^2 + bx + c = 0

e a sua solução é dada em
função dos valores de a, b e c. Podendo ter duas raízes, uma ou nenhuma. Escreva
uma função que resolva a equação do segundo grau, retornando o número de raízes
encontradas. Os valores dessas raízes devem ser retornados em parâmetros.
'''

import math

def resolve_equacao_segundo_grau(a, b, c):
    if a == 0:
        raise ValueError("O coeficiente 'a' não pode ser zero em uma equação do segundo grau.")
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return 0, None, None
    elif delta == 0:
        raiz = -b / (2*a)
        return 1, raiz, None
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return 2, raiz1, raiz2

def ler_coeficiente(mensagem):
    while True:
        try:
            coeficiente = float(input(mensagem))
            return coeficiente
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def ler_coeficientes():
    while True:
        a = ler_coeficiente("Digite o coeficiente a (diferente de zero): ")
        if a != 0:
            break
        print("O coeficiente 'a' não pode ser zero.")
    
    b = ler_coeficiente("Digite o coeficiente b: ")
    c = ler_coeficiente("Digite o coeficiente c: ")
    return a, b, c

def imprimir_resultado(num_raizes, raiz1, raiz2):
    if num_raizes == 0:
        print("A equação não possui raízes reais.")
    elif num_raizes == 1:
        print(f"A equação possui uma raiz real: {raiz1}")
    else:
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")

def main():
    a, b, c = ler_coeficientes()
    
    try:
        num_raizes, raiz1, raiz2 = resolve_equacao_segundo_grau(a, b, c)
        imprimir_resultado(num_raizes, raiz1, raiz2)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()