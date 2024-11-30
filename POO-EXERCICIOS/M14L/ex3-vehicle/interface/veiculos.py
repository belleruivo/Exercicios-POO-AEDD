<<<<<<< HEAD
from interface import InterfaceVeiculos

class Carro(InterfaceVeiculos):
    def __init__(self):
        self.carros = []
        
    def registrar(self):
        while True: 
            try:
                num_carros = int(input("Quantos carros você gostaria de adicionar?: "))
                break
            except ValueError:
                print("Por favor, insira somente números inteiros!\n")

        for i in range(num_carros):
            marca = input(f"\nQual a marca do carro {i + 1}°: ").capitalize()

            while True:
                tipo_carro = input("O carro é 1-Automático ou 2-Manual?: ")
                if tipo_carro in ["1", "2"]:
                    tipo = "Automático" if tipo_carro == "1" else "Manual"
                    break
                else: 
                    print("Por favor, escolha entre (1) e (2)\n")
            
            while True:
                possui_seguro = input("Possui seguro automotivo (S/N)?: ").lower()
                if possui_seguro in ["s", "n"]:
                    seguro = "Sim" if possui_seguro == "s" else "Não"
                    break
                else: 
                    print("Por favor, insira somente (S)-Sim ou (N)-Não\n")

            dados_carro = {
                "Marca": marca,
                "Tipo": tipo,
                "Seguro": seguro
            }
            self.carros.append(dados_carro)
        print("\nCarros registrados com sucesso!")

    def consultar_veiculo(self):
        if not self.carros:
            print("Nenhum carro registrado ainda.")
            return

        print("\nCarros Registrados:")
        for i, carro in enumerate(self.carros, start=1):
            print(f"\nCarro {i}:")
            print(f"  Marca: {carro['Marca']}")
            print(f"  Tipo: {carro['Tipo']}")
            print(f"  Seguro: {carro['Seguro']}")

        
class Caminhao(InterfaceVeiculos):
    def __init__(self):
        self.caminhoes = []
        
    def registrar(self):
        while True: 
            try:
                num_caminhoes = int(input("Quantos caminhões você gostaria de adicionar?: "))
                break
            except ValueError:
                print("Por favor, insira somente números inteiros!\n")

        for i in range(num_caminhoes):
            marca = input(f"\nQual a marca do caminhão {i + 1}°: ").capitalize()

            while True:
                try:
                    n_eixos = int(input("Quantidade de eixos: "))
                    break
                except ValueError:
                    print("Por favor, insira um número válido para os eixos\n")
            
            while True:
                possui_seguro = input("Possui seguro automotivo (S/N)?: ").lower()
                if possui_seguro in ["s", "n"]:
                    seguro = "Sim" if possui_seguro == "s" else "Não"
                    break
                else: 
                    print("Por favor, insira somente (S)-Sim ou (N)-Não\n")

            dados_caminhao = {
                "Marca": marca,
                "Quantidade de Eixos": n_eixos,
                "Seguro": seguro
            }
            self.caminhoes.append(dados_caminhao)
        print("\nCaminhões registrados com sucesso!")

    def consultar_veiculo(self):
        if not self.caminhoes:
            print("Nenhum caminhão registrado ainda.")
            return

        print("\nCaminhões Registrados:")
        for i, caminhao in enumerate(self.caminhoes, start=1):
            print(f"\nCaminhão {i}:")
            print(f"  Marca: {caminhao['Marca']}")
            print(f"  Quantidade de Eixos: {caminhao['Quantidade de Eixos']}")
            print(f"  Seguro: {caminhao['Seguro']}")
=======
from interface import Vehicle, GPS

class Car(Vehicle, GPS):
    def start_engine(self):
        print("Motor do carro ligado.")

    def move(self):
        print("O carro está se movendo sobre rodas.")
    
    def get_location(self):
        print("O carro está localizado na Rua Faria Lima em São Paulo")

    def get_altitude(self):
        print("O carro está a uma altitude de 1.200 metros acima do nível do mar")

class Airplane(Vehicle, GPS):
    def start_engine(self):
        print("Motores do avião ligados.")

    def move(self):
        print("O avião está voando pelo céu.")

    def get_location(self):
        print("O avião está localizado nas coordenadas 40° N, 74° W.")

    def get_altitude(self):
        print("Altitude atual do avião: 10.000 metros acima do nível do mar")
>>>>>>> 8d4c7a5a5e476c0d2f16b37e02f1281d78c4562b
