''' 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
acesso e impressão para esta classe e faça um programa de teste.
'''

class Vehicle:
    def __init__(self, velocidade, direção, nome):
        self.velocidade = velocidade
        self.direcao = direção
        self.nome = nome
        
    #métodos de acesso
    def getVelocidade(self):
        return self.velocidade
    
    def getDireção(self):
        return self.direção
    
    def getNome(self):
        return self.nome

    #métodos de modificação
    def setVelocidade(self, velocidade):
        self.velocidade = velocidade
        
    def setDireção(self, direção):
        self.direção = direção
        
    def setNome(self, nome):
        self.nome = nome
        
    def imprimir(self):
        print("\nDetalhes do Veículo:")
        print(f"Velocidade Atual: {self.velocidade} km/h")
        print(f"Direção dos Pneus: {self.direcao}°")
        print(f"Nome do Proprietário: {self.nome}")
        

def main():
    while True:
        try:
            velocidade = float(input("Digite a velocidade atual (km/h): "))
            direcao = float(input("Digite a direção dos pneus (graus): "))
            nome = input("Digite o nome do proprietário: ")
            break
            
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir números válidos para velocidade e direção.\n")
            return
    
    carro = Vehicle(velocidade, direcao, nome)
        
    carro.imprimir()
        
        
main()