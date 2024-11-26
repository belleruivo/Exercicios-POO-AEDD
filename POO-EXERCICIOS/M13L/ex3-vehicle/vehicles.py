from abc import ABC, abstractmethod

class Veiculos(ABC):
    @abstractmethod
    def registrar(self):
        pass
    
    @abstractmethod
    def consultar_veiculo(self):
        pass


class Carro(Veiculos):
    def __init__(self):
        self.carros = []
        
    def registrar(self):
        num_carros = int(input("Quantos carros você gostaria de adicionar?: "))
        for i in range(num_carros):
            marca_carro = input(f"Qual a marca do carro {i+1}°: ").capitalize()
            while True:
                try:
                    tipo_carro = int(input("O carro é 1-automático ou 2-manual?: "))
                    if tipo_carro in [1, 2]:
                        break
                    else: 
                        print("Por favor escolher entre (1) e (2)")
                except ValueError:
                    print("Por favor escolher entre (1) e (2)")
            
            seguro_carro = input("Possui seguro automotivo (S/N)?: ").lower()
            
            tipo = "Automático" if tipo_carro == 1 else "Manual"
            possui_seguro = True if seguro_carro == 's' else False

            dados_carro = {
                "Marca do Carro": marca_carro,
                "Tipo": tipo,
                "Seguro": possui_seguro
            }
            self.carros.append(dados_carro)
        print("\nCarros registrados com sucesso!")
            
    def consultar_veiculo(self):
        if not self.carros:
            print("Nenhum carro registrado ainda.")
            return

        print("\nCarros Registrados:")
        for i, carro in enumerate(self.carros, start=1):
            print(f"Carro {i}:")
            print(f"  Marca: {carro['Marca do Carro']}")
            print(f"  Tipo: {carro['Tipo']}")
            print(f"  Seguro: {carro['Seguro']}")


class Caminhao(Veiculos):
    def __init__(self):
        self.caminhoes = []
        
    def registrar(self):
        num_caminhoes = int(input("Quantos caminhões você gostaria de adicionar?: "))
        for i in range(num_caminhoes):
            marca_caminhao = input(f"Qual a marca do caminhão {i+1}°: ").capitalize()
            try:
                n_eixos = int(input("Quantidade de eixos: "))
            except ValueError:
                print("Por favor, certifique-se de inserir o número de eixos corretamente")
            seguro_caminhao = input("Possui seguro automotivo (S/N)?: ").lower()
            possui_seguro = True if seguro_caminhao == 's' else False

            dados_caminhao = {
                "Marca do Caminhão": marca_caminhao,
                "Quantidade de Eixos": n_eixos,
                "Seguro": possui_seguro
            }
            self.caminhoes.append(dados_caminhao)
        print("\nCaminhões registrados com sucesso!")

    def consultar_veiculo(self):
        if not self.caminhoes:
            print("Nenhum caminhão registrado ainda.")
            return

        print("\nCaminhões Registrados:")
        for i, caminhao in enumerate(self.caminhoes, start=1):
            print(f"Caminhão {i}:")
            print(f"  Marca: {caminhao['Marca do Caminhão']}")
            print(f"  Tipo: {caminhao['Tipo']}")
            print(f"  Seguro: {caminhao['Seguro']}")