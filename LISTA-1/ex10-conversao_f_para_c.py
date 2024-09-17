'''
10. A convenção de graus Fahrenheit para Celsius é obtida pela fórmula C = 5. (F − 32)/9.
Escreva um programa que calcule e imprima uma tabela de graus centígrados em
função de graus Fahrenheit que variem de 50 a 150 de 5 em 5. Utilize constantes
simbólicas para indicar o início (50) e o fim (150) do intervalo, além do passo (5).
'''

print("-"*65)
print("Olá, seja bem-vindo(a) ao programa que converte graus Fahrenheit para Celsius!")
print("-"*65)

INICIO = 50
FIM = 150
PASSO = 5

def fahrenheit_para_celsius(fahrenheit):
    return 5 * (fahrenheit - 32) / 9

print(f"{'Fahrenheit':>12} {'Celsius':>12}")

# i = 50, condicao 150+1, +5
for fahrenheit in range(INICIO, FIM + 1, PASSO):
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit:>12} {celsius:>12.2f}")