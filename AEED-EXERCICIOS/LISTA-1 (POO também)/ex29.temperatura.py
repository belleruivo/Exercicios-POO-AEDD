''' 29. Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo: C = 5/9*(F-32). A seguir, faça um programa que, em
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC.
'''
def FparaC(f):
    c = 5/9*(f-32)
    
    return c

def main():
    print("-="*10, "CONVERTENDO FAHRENHEIT PARA CELSIUS", "-="*10)
    print("Insira a tempertaura em fahrenheit ou digite (enter) para finalizar\n")
    while True:
        try:
            entrada = input("Insira a temperatura (°F): ")
            if entrada == "":
                break
            f = float(entrada)
            print(f"A temperatura {f}°F em Celsius é de {FparaC(f):.2f}°C\n")
        except ValueError:
            print("Por favor, insira um caractere numérico.\n")
    print("-="*39)

main()