'''
20. Elabore um outro programa didático nos mesmos moldes do anterior para treino da
divisão. Neste programa deve ser perguntado à criança o resultado da divisão e o
resto.
'''
import random

print("-="*10, "BEM VINDO AO PROGRAMA DE DIVISÕES", "-="*10)

def obter_dividendo():
    while True:
        try:
            dividendo = int(input('\nEscolha o número que quer dividir (1 a 100): '))
            if dividendo > 1 and dividendo <100:
                return dividendo
            else:
                print("Por favor, insira um número entre 0 e 100.")
        except ValueError:
            print("Por favor, insira um número inteiro!")


def gerar_divisor():
    return random.randint(1, 20)


def obter_resposta(dividendo, divisor):
    while True:
        try:
            resultado = int(input(f"Qual o resultado inteiro da divisão? {dividendo} ÷ {divisor}: "))
            resto = int(input("Qual o resto da divisão?: "))
            return resultado, resto
        except ValueError:
            print("\nInsira caracteres numéricos inteiros.")


def verificar_resposta(dividendo, divisor, resultado, resto):
    return resultado == dividendo // divisor and resto == dividendo % divisor


def exibir_resultados(respostas, acertos, erros):
    print()
    print(f"-="*16, "RESULTADOS", "-="*16)
    print(f"Perguntas respondidas: {respostas}")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")
    print("-="*38)


def main():
    acertos = erros = respostas = 0
    
    while True:
        dividendo = obter_dividendo()
        divisor = gerar_divisor()
        resultado, resto = obter_resposta(dividendo, divisor)
        respostas += 1

        if verificar_resposta(dividendo, divisor, resultado, resto):
            print("\nParabéns! Você acertou a resposta.")
            acertos += 1
        else:
            print("\nQue pena! Sua resposta está incorreta.")
            erros += 1

        while True: 
            continuar = input("Deseja continuar? (S/N): ").upper()
            if continuar == "N" or continuar == "S":
                break
            else:
                print("\nDigite somente (S) para sim ou (N) para não")

        if continuar == "N":
            break


   
    exibir_resultados(respostas, acertos, erros)



if __name__ == "__main__":
    main()
    





    



 