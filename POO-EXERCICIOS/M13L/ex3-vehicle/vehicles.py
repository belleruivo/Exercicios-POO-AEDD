from classeAbstrata import Vehicle

class Carro(Vehicle):
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
            self.veiculos.append(dados_carro)
        print("\nCarros registrados com sucesso!")


class Caminhao(Vehicle):
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
            self.veiculos.append(dados_caminhao)
        print("\nCaminhões registrados com sucesso!")



