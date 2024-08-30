'''
14. Construa um programa que calcule e mostre a soma dos 30 primeiros termos da
série: 450/10 + 445/11 + 440/12 + 435/13 + ...
'''

def soma():
    numerador = 450
    denominador = 10
    termo = 1
    soma = 0

    while termo <= 30:
        valor_termo = numerador / denominador
        numerador -= 5
        denominador += 1
        soma += valor_termo
        termo+= 1
    
    return soma

print(f"\nA soma dos 30 primeiros termos da série é: {soma()}\n")


