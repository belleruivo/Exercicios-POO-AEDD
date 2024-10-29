class Consumo:
    def __init__(self, valor_combustivel, consumo_por_km, gps): 
        self.valor_combustivel = valor_combustivel
        self.consumo_por_km = consumo_por_km  
        self.gps = gps #um atributo que armazena uma instância da classe GPS

    def set_combustivel(self, valor_combustivel):
        self.valor_combustivel = valor_combustivel

    def get_combustivel(self):
        return self.valor_combustivel
    
    def set_consumo_por_km(self, consumo_por_km):
        self.consumo_por_km = consumo_por_km
    
    def get_consumo_por_km(self):
        return self.consumo_por_km
    
    def calcular_custo_viagem(self):
        distancia = self.gps.get_distancia() #utiliza o método get_distancia da classe gps
        custo_total = (distancia / self.consumo_por_km) * self.valor_combustivel
        return custo_total
    
    def imprimir(self):
        distancia = self.gps.get_distancia()
        custo = self.calcular_custo_viagem()
        print(f"Distância total: {distancia}Km")
        print(f"Custo total da viagem: R${custo:.2f}")