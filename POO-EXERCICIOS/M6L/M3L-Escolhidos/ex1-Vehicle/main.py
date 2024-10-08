from vehicle import Vehicle
from gps import GPS

def main():
    print("-="*40)
    print("INSIRA SUAS INFORMAÇÕES:")
    while True:
        try:
            velocidade = float(input("\nDigite a velocidade atual do veículo (km/h): "))
            if velocidade < 0:
                print("A velocidade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir somente caracteres numéricos.\n")
            
    while True:
        try:
            direção = float(input("Digite a direção dos pneus (graus): "))
            if direção < 0 or direção >= 360:
                print("A direção deve estar entre 0 e 360 graus. Tente novamente.\n")
                continue
            break
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir somente carateres numéricos.\n")

    while True:
        nome = input("Digite o nome do proprietário: ")
        if nome.replace(" ", "").isalpha():
            break
        print("Nome inválido. Certifique-se de inserir somente letras.\n")

    while True:
        localizacao = input("Insira a localização atual: ")
        if localizacao.replace(" ", "").isalpha():
            break
        print("Localização inválida. Certifique-se de inserir somente letras.\n")

    while True:
        destino = input("Insira o nome do destino: ")
        if destino.replace(" ", "").isalpha():
            break
        print("Destino inválido. Certifique-se de inserir somente letras.\n")
    
    gps = GPS(localizacao, destino)
    veiculo = Vehicle(velocidade, direção, nome, gps)

    veiculo.imprimir()    
        
main()