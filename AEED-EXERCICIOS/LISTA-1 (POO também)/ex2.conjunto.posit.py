''' 
2. Faça um programa que leia um conjunto de números positivos, sendo o conjunto destes números finalizado
quando for digitado um número negativo. Ao final, imprima o maior e o menor número lido e a média deles.
'''

def main():
    maior_numero = None
    menor_numero = None
    soma = 0
    quantidade = 0

    while True:
        try:
            numero = float(input("Digite um número positivo (ou um número negativo para finalizar): "))

            if numero < 0:
                break

            if maior_numero is None or numero > maior_numero:
                maior_numero = numero

            if menor_numero is None or numero < menor_numero:
                menor_numero = numero

            soma += numero
            quantidade += 1

        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    if quantidade > 0:
        media = soma / quantidade
        print(f"Maior número: {maior_numero}")
        print(f"Menor número: {menor_numero}")
        print(f"Média dos números: {media:.2f}")
    else:
        print("Nenhum número positivo foi inserido.")

main()