from invoice import Invoice

class Store:
    def __init__(self):
        self.faturas = []  # Lista para armazenar faturas

    def adicionar_fatura(self, numero_item, descricao, quantidade, preco_unitario):
        fatura = Invoice(numero_item, descricao, quantidade, preco_unitario)
        self.faturas.append(fatura)

    def calcular_total_faturas(self):
        return sum(fatura.calcular_valor_fatura() for fatura in self.faturas)

    def exibir_faturas(self):
        print("\nDetalhes das faturas:")
        for fatura in self.faturas:
            print(f"\nNúmero do item: {fatura.get_numero_item()}")
            print(f"Descrição do item: {fatura.get_descricao()}")
            print(f"Quantidade comprada: {fatura.get_quantidade()}")
            print(f"Preço unitário: {fatura.get_preco_unitario():.2f}")
            print(f"Valor total da fatura: {fatura.calcular_valor_fatura():.2f}")

    @staticmethod
    def obter_entrada(mensagem, tipo=float):
        while True:
            try:
                if tipo == int:
                    return int(input(mensagem))
                else:
                    return float(input(mensagem))
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico.\n")
