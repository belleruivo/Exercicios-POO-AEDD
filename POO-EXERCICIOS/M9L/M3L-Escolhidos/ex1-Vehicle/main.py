from proprietario import Proprietario
from carro import Carro

def main():
    print("-=" * 40)
    print("INSIRA SUAS INFORMAÇÕES:")

    while True:
        nome = input("\nDigite o nome do proprietário: ")
        if nome.replace(" ", "").isalpha():
            break
        print("Nome inválido. Certifique-se de inserir somente letras.")
    owner = Proprietario(nome)

    while True:
        while True:
            try:
                velocidade = int(input("\nDigite a velocidade atual do veículo (km/h): "))
                if velocidade < 0:
                    print("A velocidade não pode ser negativa. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir somente caracteres numéricos inteiros.")

        while True:
            try:
                direcao = float(input("Digite a direção dos pneus (graus): ").replace(",", "."))
                if direcao < 0 or direcao >= 360:
                    print("A direção deve estar entre 0 e 360 graus. Tente novamente.\n")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir somente caracteres numéricos.\n")

        carro = Carro(velocidade, direcao, owner) 

        while True:
            adicionar_mais = input("Deseja adicionar outro veículo? (s/n): ").lower()
            if adicionar_mais in ['s', 'n']:
                break  
            else:
                print("Resposta inválida. Por favor, insira 's' para sim ou 'n' para não.\n")
    
        if adicionar_mais != 's':
            break

    owner.imprimir_veiculos()
    print("-=" * 40)

main()