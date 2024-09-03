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

def sen(a):
    for c in range(0, 100):
        
    return 

