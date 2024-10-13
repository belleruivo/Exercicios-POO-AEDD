class Fatura:
    def __init__(self, numero_item, descricao, quantidade, preco_unitario):
        self.numero_item = numero_item
        self.descricao = descricao
        self.quantidade = max(0, quantidade)
        self.preco_unitario = max(0.0, preco_unitario)

    def calcular_valor_fatura(self):
        return self.quantidade * self.preco_unitario

    @staticmethod
    def obter_entrada(mensagem, tipo=float):
        while True:
            entrada = input(mensagem).replace(',', '.')  # Substitui vírgula por ponto
            try:
                if tipo == int:
                    return int(entrada)
                else:
                    return float(entrada)
            except ValueError:
                if tipo == int:
                    print("Erro: Por favor, insira um número inteiro válido.\n")
                else:
                    print("Erro: Por favor, insira um valor numérico válido.\n")


class FaturaComImposto(Fatura):
    def __init__(self, fatura: Fatura, taxa_imposto):
        super().__init__(fatura.numero_item, fatura.descricao, fatura.quantidade, fatura.preco_unitario)
        self.taxa_imposto = max(0.0, taxa_imposto)

    def calcular_valor_fatura_com_imposto(self):
        return self.calcular_valor_fatura() * (1 + self.taxa_imposto / 100)

