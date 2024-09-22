''' 32. O seno de um ângulo em radianos, no intervalo de 0 à π/2
pode ser calculado através da série de McLaurin, apresentada a seguir:
senx = x/1! - (x**3)/3! + (x**5)/5! - (x**7)/7! + ...

a. Escreva uma função que converta um ângulo em graus para seu valor em
radianos (180 = πrad)
b. Escreva uma função que receba como parâmetro um ângulo em graus, a
precisão requerida para o cálculo e retorne o seu seno, utilizando a função de conversão graus-radiano feita anteriormente
c. Faça um programa que teste a sua função para cálculo do seno.
'''
import math

def radianos(angulo):
    return angulo * (math.pi / 180)

def fatorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

def sen(a, precisao):
    a_rad = radianos(a)
    
    seno = 0
    
    for n in range(precisao):
        termo = ((-1) ** n) * (a_rad ** (2 * n + 1)) / fatorial(2 * n + 1)
        seno += termo
        
    return seno

def main():
    while True:
        try:
            angulo = float(input("Digite o ângulo em graus: "))
            break
        except ValueError:
            print("Digite um número válido para o ângulo!\n")
    
    while True:
        try:
            precisao = int(input("Digite a precisão (número de termos da série de McLaurin): "))
            break
        except ValueError:
            print("Digite um número inteiro válido para a precisão!\n")

    seno = sen(angulo, precisao)
    print(f"\nO seno aproximado de {angulo} graus é: {seno}")
            
    seno_real = math.sin(radianos(angulo))
    print(f"O valor real do seno calculado por math.sin é: {seno_real}")

main()

