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

class ItemFatura:
    def __init__(self, descricao, quantidade, preco_por_item):
        self.descricao = descricao
        self.quantidade = ValidadorFatura.validar_quantidade(quantidade)
        self.preco_por_item = ValidadorFatura.validar_preco(preco_por_item)

    def calcular_valor(self):
        return self.quantidade * self.preco_por_item

class Fatura:
    def __init__(self, numero, descricao):
        self._numero = numero
        self._descricao = descricao
        self.itens = []

    def set_numero(self, numero):
        self._numero = numero

    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_numero(self):
        return self._numero

    def get_descricao(self):
        return self._descricao

    def adicionar_item(self, descricao, quantidade, preco_por_item):
        item = ItemFatura(descricao, quantidade, preco_por_item)
        # Adiciona o item à lista de itens da fatura
        self.itens.append(item)

    def calcular_valor_fatura(self):
        return sum(item.calcular_valor() for item in self.itens)

def main():
    fatura1 = Fatura("12345", "Mouse sem fio")
    fatura1.adicionar_item("Mouse sem fio", 2, 50.0)
    print(f"Número da fatura: {fatura1.get_numero()}")
    print(f"Descrição: {fatura1.get_descricao()}")
    item1 = fatura1.itens[0]  # Acessa o primeiro item
    print(f"Quantidade: {item1.quantidade}, Preço por item: R$ {item1.preco_por_item:.2f}")
    print(f"Valor total da fatura: R$ {fatura1.calcular_valor_fatura():.2f}")

    fatura2 = Fatura("54321", "Teclado mecânico")
    fatura2.adicionar_item("Teclado mecânico", -3, 150.0)  
    print(f"\nNúmero da fatura: {fatura2.get_numero()}")
    print(f"Descrição: {fatura2.get_descricao()}")
    if fatura2.itens:  # Verifica se existem itens
        item2 = fatura2.itens[0]
        print(f"Quantidade: {item2.quantidade}, Preço por item: R$ {item2.preco_por_item:.2f}")
    print(f"Valor total da fatura: R$ {fatura2.calcular_valor_fatura():.2f}")

    fatura3 = Fatura("67890", "Monitor LED")
    fatura3.adicionar_item("Monitor LED", 1, -350.0)       
    print(f"\nNúmero da fatura: {fatura3.get_numero()}")
    print(f"Descrição: {fatura3.get_descricao()}")
    if fatura3.itens:  # Verifica se existem itens
        item3 = fatura3.itens[0]
        print(f"Quantidade: {item3.quantidade}, Preço por item: R$ {item3.preco_por_item:.2f}")
    print(f"Valor total da fatura: R$ {fatura3.calcular_valor_fatura():.2f}")

main()
