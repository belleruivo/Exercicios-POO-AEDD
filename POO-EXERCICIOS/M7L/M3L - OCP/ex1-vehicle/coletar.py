from vehicleDetalhado import VehicleDetalhado

class VehicleColetarDados:
    # Validação e coleta de dados em métodos estáticos separados
    @staticmethod
    def validar_velocidade():
        while True:
            try:
                velocidade = float(input("\nDigite a velocidade atual do veículo (km/h): "))
                if velocidade < 0:
                    print("A velocidade não pode ser negativa. Tente novamente.")
                    continue
                return velocidade
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir somente caracteres numéricos.\n")
    
    @staticmethod
    def validar_direção():
        while True:
            try:
                direção = float(input("Digite a direção dos pneus (graus): "))
                if direção < 0 or direção >= 360:
                    print("A direção deve estar entre 0 e 360 graus. Tente novamente.\n")
                    continue
                return direção
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir somente caracteres numéricos.\n")
                
    @staticmethod
    def validar_nome():
        while True:
            nome = input("Digite o nome do proprietário: ")
            if nome.replace(" ", "").isalpha():
                return nome
            print("Nome inválido. Certifique-se de inserir somente letras.\n")
        
    @staticmethod
    def coletar_dados():
        velocidade = VehicleColetarDados.validar_velocidade()
        direção = VehicleColetarDados.validar_direção()
        nome = VehicleColetarDados.validar_nome()
        
        return VehicleDetalhado(velocidade, direção, nome)
