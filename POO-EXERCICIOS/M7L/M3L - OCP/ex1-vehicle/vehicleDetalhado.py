from vehicle import Vehicle

class VehicleDetalhado(Vehicle): #Associação de classes?
    # Classe filha que adiciona funcionalidades extras, mantendo Vehicle inalterada.
    def exibir_detalhes(self):
        return (
            f"Velocidade Atual: {self.get_velocidade()} km/h\n"
            f"Direção dos Pneus: {self.get_direção()}°\n"
            f"Nome do Proprietário: {self.get_nome()}"
        )