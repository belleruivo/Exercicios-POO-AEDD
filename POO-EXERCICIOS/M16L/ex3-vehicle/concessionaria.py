from veiculos import VehicleAction

class Concessionaria:
    def __init__(self):
        self.lista_veiculos = []

    def registrar_veiculo(self, veiculo: VehicleAction):
        self.lista_veiculos.append(veiculo)

    def vender_veiculo(self, id_veiculo: int):
        if 0 <= id_veiculo < len(self.lista_veiculos):
            veiculo_vendido = self.lista_veiculos.pop(id_veiculo)
            print(veiculo_vendido.vender())
        else:
            print("Veículo não encontrado!")

    def listar_veiculos(self):
        if not self.lista_veiculos:
            print("Nenhum veículo registrado!")
        for i, veiculo in enumerate(self.lista_veiculos, 1):
            print(f"{i}. {veiculo.obter_informacoes()}")
