''' 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
acesso e impressão para esta classe e faça um programa de teste.
'''
class Vehicle:
    def __init__(self, velocidade, direção, nome):
        self.velocidade = velocidade
        self.direção = direção
        self.nome = nome
                                                                                                                                               
    def getVelocidade(self):
        return self.velocidade
    
    def getDireção(self):
        return self.direção
    
    def getNome(self):
        return self.nome

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade
        
    def setDireção(self, direção):
        self.direção = direção
        
    def setNome(self, nome):
        self.nome = nome
        
    def imprimir(self):
        print("-"*40)
        print("         DETALHES DO VEÍCULO:")
        print("-"*40)
        print(f"Velocidade Atual: {self.velocidade}km/h")
        print(f"Direção dos Pneus: {self.direção}°")
        print(f"Nome do Proprietário: {self.nome}")
        print("-"*40)

        

def main():
    print("-"*40)
    print("          INSIRA SUAS INFORMAÇÕES:")
    print("-"*40)
    
    while True:
        try:
            velocidade = float(input("Digite a velocidade atual do veículo (km/h): "))
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
    
    carro = Vehicle(velocidade, direção, nome)   
    carro.imprimir()
        
main()