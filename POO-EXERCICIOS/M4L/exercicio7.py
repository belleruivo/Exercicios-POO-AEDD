# Crie uma classe Invoice para que uma loja de suprimentos de informática possa
# utilizá-la para representar a fatura de um item vendido na loja. Uma Invoice deve
# incluir quatro variáveis de instância: o número da fatura (string), a descrição (string),
# a quantidade comprada de um item (int) e o preço por item (float). Sua classe deve ter
# um construtor que inicializa as quatro variáveis de instância. Forneça um método set
# e um get para cada variável de instância. Forneça também um método chamado que
# calcula o valor da fatura (multiplica preço por quantidade do item) e retorna o
# resultado. Se a quantidade de itens passada pelo usuário não for positiva, deve ser
# configurada como 0. Se o preço do item não for positivo, deve ser configurado como
# 0.0. Teste a classe implementada e seus métodos.

class ValidadorFatura:
    @staticmethod
    def validar_quantidade(quantidade):
        return max(0, quantidade)

    @staticmethod
    def validar_preco(preco):
        return max(0.0, preco)  

class CalculadoraFatura:
    @staticmethod
    def calcular_valor(quantidade, preco_por_item):
        return quantidade * preco_por_item

class Fatura:
    def __init__(self, numero, descricao, quantidade, preco_por_item):
        self.set_numero(numero)
        self.set_descricao(descricao)
        self.set_quantidade(quantidade)
        self.set_preco_por_item(preco_por_item)

    def set_numero(self, numero):
        self._numero = numero

    def set_descricao(self, descricao):
        self._descricao = descricao

    def set_quantidade(self, quantidade):
        self._quantidade = ValidadorFatura.validar_quantidade(quantidade)

    def set_preco_por_item(self, preco_por_item):
        self._preco_por_item = ValidadorFatura.validar_preco(preco_por_item)

    def get_numero(self):
        return self._numero

    def get_descricao(self):
        return self._descricao

    def get_quantidade(self):
        return self._quantidade

    def get_preco_por_item(self):
        return self._preco_por_item

    def calcular_valor_fatura(self):
        return CalculadoraFatura.calcular_valor(self._quantidade, self._preco_por_item)

def main():
    fatura1 = Fatura("12345", "Mouse sem fio", 2, 50.0)
    print("Número da fatura: {}".format(fatura1.get_numero()))
    print("Descrição: {}".format(fatura1.get_descricao()))
    print(f"Quantidade: {fatura1.get_quantidade()}")
    print(f"Preço por item: R$ {fatura1.get_preco_por_item():.2f}")
    print(f"Valor total da fatura: R$ {fatura1.calcular_valor_fatura():.2f}")

    fatura2 = Fatura("54321", "Teclado mecânico", -3, 150.0)
    print(f"\nNúmero da fatura: {fatura2.get_numero()}")
    print(f"Descrição: {fatura2.get_descricao()}")
    print(f"Quantidade: {fatura2.get_quantidade()}")
    print(f"Preço por item: R$ {fatura2.get_preco_por_item():.2f}")
    print(f"Valor total da fatura: R$ {fatura2.calcular_valor_fatura():.2f}")

    fatura3 = Fatura("67890", "Monitor LED", 1, -450.0)
    print(f"\nNúmero da fatura: {fatura3.get_numero()}")
    print(f"Descrição: {fatura3.get_descricao()}")
    print(f"Quantidade: {fatura3.get_quantidade()}")
    print(f"Preço por item: R$ {fatura3.get_preco_por_item():.2f}")
    print(f"Valor total da fatura: R$ {fatura3.calcular_valor_fatura():.2f}")

main()