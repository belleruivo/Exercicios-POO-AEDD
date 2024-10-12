class Invoice:
    def __init__(self, numero_item, descricao, quantidade, preco_unitario):
        self.numero_item = numero_item
        self.descricao = descricao
        self.quantidade = max(0, quantidade)  
        self.preco_unitario = max(0.0, preco_unitario) 

    @property
    def numero_item(self):
        return self._numero_item

    @numero_item.setter
    def numero_item(self, value):
        self._numero_item = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = max(0, value)

    @property
    def preco_unitario(self):
        return self._preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, value):
        self._preco_unitario = max(0.0, value)

    def calcular_valor_fatura(self):
        return self.quantidade * self.preco_unitario
