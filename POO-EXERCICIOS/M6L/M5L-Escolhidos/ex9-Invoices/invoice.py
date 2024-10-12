class Invoice:
    def __init__(self, numero_item, descricao, quantidade, preco_unitario):
        self.numero_item = numero_item
        self.descricao = descricao
        self.quantidade = max(0, quantidade)  # Garantir que a quantidade não seja negativa
        self.preco_unitario = max(0.0, preco_unitario)  # Garantir que o preço não seja negativo

    def get_numero_item(self):
        return self.numero_item

    def get_descricao(self):
        return self.descricao

    def get_quantidade(self):
        return self.quantidade

    def get_preco_unitario(self):
        return self.preco_unitario

    def set_numero_item(self, numero_item):
        self.numero_item = numero_item

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_quantidade(self, quantidade):
        self.quantidade = max(0, quantidade)

    def set_preco_unitario(self, preco_unitario):
        self.preco_unitario = max(0.0, preco_unitario)

    def calcular_valor_fatura(self):
        return self.quantidade * self.preco_unitario
