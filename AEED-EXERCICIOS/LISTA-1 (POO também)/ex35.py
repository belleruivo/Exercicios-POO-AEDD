'''
35. Faça um programa que apresente na tela um menu com as seguintes opções: 1. Converter um ângulo em graus para radiano; 
2. Calcular o seno de um ângulo, 3. Calcular o valor de π. 4. Resolver uma equação do segundo grau; 
0. Sair. Depois de feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros
necessários para o cálculo escolhido e a seguir usar uma das funções que você já implementou.
'''
import math

def radianos(angulo):
    return angulo * (math.pi / 180)

def sen(angulo):
    return math.sin(angulo)

def pi():
    return math.pi
    
def equação_segundo(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        
        return (x1, x2)
    
    elif delta == 0:
        x = -b / (2 * a)
        return (x,)
    
def main():
    print("-="*15, "MENU", "-="*15)
    while True:

        try:
            print("""
    (1) - Converter um ângulo em graus para radiano
    (2) - Calcular o seno de um ângulo
    (3) - Calcular o valor de π
    (4) - Resolver uma equação do segundo grau
    (0) - Sair""")
            
            escolha = int(input("\nEscolha uma das opções: "))
            
            if escolha == 1:
                angulo = float(input("Digite o ângulo em graus: "))
                print(f"\nO radiano de {angulo} é: {radianos(angulo):.2f}")
                
            elif escolha == 2:
                angulo = float(input("Digite o ângulo em graus: "))
                print(f"\nSen de {angulo}: {sen(angulo):.2f}")
                
            elif escolha == 3:
                print(f"\nO valor de π é: {pi():.2f}")
                
            elif escolha == 4:
                a = float(input("\nDigite o valor de A da equação: "))
                b = float(input("Digite o valor de B da equação: "))
                c = float(input("Digite o valor de C da equação: "))
                print(f"\nO valor de (x1, x2) é: {equação_segundo(a, b, c)}")
            elif escolha == 0:
                break
            
            else:
                print("Por favor, escolha uma opção válida!")

        except ValueError:
            print("Por favor, escolha uma opção válida")
            
    print("-="*8, "Finalizando...", "-="*8)
main()