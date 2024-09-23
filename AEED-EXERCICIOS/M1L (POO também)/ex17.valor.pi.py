'''
17. O número pi pode ser calculado através da série: pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ... Faça um
programa para calcular o valor de pi com precisão de 0,00001 (o programa encerra
quando a parcela da série for menor que a precisão).
'''

def num_pi(precisao):
    numerador = 4
    denominador = 1
    sinal = 1
    resul = 0

    while True:
        termo = (numerador/denominador)*sinal
        resul = resul+termo

        if abs(termo) < precisao:
            break

        sinal *= -1
        denominador += 2
    
    return resul

def main():
    precisao = 0.00001
    print(f"\nO número de pi com precisão 0,00001 é: {num_pi(precisao)}\n")

main()