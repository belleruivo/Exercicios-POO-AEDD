'''
19. Faça um programa didático para estudo de tabuadas de 1 até 10, onde:
a. A criança escolhe a tabuada a ser estudada.
b. O programa gera um número aleatório e pergunta à criança qual o valor dele
multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta
novamente, se acertar o programa pergunta à criança se ela deseja continuar
respondendo.
c. Ao final, o programa deve imprimir o número de perguntas respondidas, o
número de acertos e o número de erros cometidos pela criança.
'''

import random

def escolher_tabuada():
    while True:
        try:
            tabuada = int(input("Escolha a tabuada (1 a 10): "))
            if 1 <= tabuada <= 10:
                return tabuada
            else:
                print("Por favor, escolha um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def gerar_pergunta(tabuada):
    numero = random.randint(1, 10)
    while True:
        try:
            resposta = int(input(f"Qual é o resultado de {tabuada} x {numero}? "))
            return numero, resposta
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def verificar_resposta(tabuada, numero, resposta):
    return resposta == tabuada * numero

def deseja_continuar():
    while True:
        continuar = input("Você deseja continuar? (s/n): ").strip().lower()
        if continuar in ['s', 'n']:
            return continuar == 's'
        else:
            print("Entrada inválida. Por favor, responda com 's' para sim ou 'n' para não.")

def imprimir_resultados(perguntas, acertos, erros):
    print(f"\nResultados:")
    print(f"Perguntas respondidas: {perguntas}")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")

def main():
    perguntas = 0
    acertos = 0
    erros = 0

    tabuada = escolher_tabuada()

    while True:
        numero, resposta = gerar_pergunta(tabuada)
        perguntas += 1

        if verificar_resposta(tabuada, numero, resposta):
            acertos += 1
            print("Correto!")
            if not deseja_continuar():
                break
        else:
            erros += 1
            print("Errado! Tente novamente.")

    imprimir_resultados(perguntas, acertos, erros)

if __name__ == "__main__":
    main()