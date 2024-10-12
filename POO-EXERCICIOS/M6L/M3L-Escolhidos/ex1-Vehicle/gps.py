class GPS:
    def __init__(self, localizacao_atual, destino, distancia):
        self.localizacao_atual = localizacao_atual
        self.destino = destino
        self.distancia = distancia

    def set_localizacao(self, localizacao_atual):
        self.localizacao_atual = localizacao_atual
        
    def set_destino(self, destino):
        self.destino = destino

    def set_distancia(self, distancia):
        self.distancia = distancia

    def get_distancia(self):
        return self.distancia
        
    def get_localizacao(self):
        return self.localizacao_atual
    
    def get_destino(self):
        return self.destino
    
    def imprimir(self):
        print(f"Localização Atual: {self.localizacao_atual}")
        print(f"Destino: {self.destino}")
        print(f"A distância entre as duas cidades é de: {self.distancia}Km")