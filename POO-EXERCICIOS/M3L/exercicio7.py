# Crie uma classe Fatura para que uma loja de suprimentos de informática possa
# utilizá-la para representar a fatura de um item vendido na loja. Uma Fatura deve
# incluir quatro variáveis de instância: o número da fatura (string), a descrição (string),
# a quantidade comprada de um item (int) e o preço por item (float). Sua classe deve ter
# um construtor que inicializa as quatro variáveis de instância.
# Forneça um método set e um get para cada variável de instância. Forneça também um método chamado que
# calcula o valor da fatura (multiplica preço por quantidade do item) e retorna o
# resultado. Se a quantidade de itens passada pelo usuário não for positiva, deve ser
# configurada como 0. Se o preço do item não for positivo, deve ser configurado como
# 0.0. Teste a classe implementada e seus métodos.

print("-" * 42)
print("    FATURA DA LOJA DE INFORMÁTICA")
print("-" * 42)

class Fatura:
    def __init__(self, numFatura, descricao, quantidade, precoItem):
        self.numFatura = numFatura
        self.descricao = descricao
        self.quantidade = quantidade if quantidade > 0 else 0
        self.precoItem = precoItem if precoItem > 0 else 0.0

    def get_numFatura(self):
        return self.numFatura

    def set_numFatura(self, numFatura):
        self.numFatura = numFatura

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade if quantidade > 0 else 0

    def get_preco_por_item(self):
        return self.precoItem

    def set_preco_por_item(self, precoItem):
        self.precoItem = precoItem if precoItem > 0 else 0.0

    def calcular_fatura(self):
        return self.quantidade * self.precoItem

def main():
    numFatura = "A123"
    descricao = "Teclado"
    quantidade = 5
    precoItem = 50.0

    fatura = Fatura(numFatura, descricao, quantidade, precoItem)

    print(f"NÚMERO DA FATURA: {fatura.get_numFatura()}")
    print(f"DESCRIÇÃO: {fatura.get_descricao()}")
    print(f"QUANTIDADE: {fatura.get_quantidade()}")
    print(f"PREÇO POR ITEM: R$ {fatura.get_preco_por_item():.2f}")
    print(f"VALOR DA FATURA: R$ {fatura.calcular_fatura():.2f}")

    print()
    fatura.set_quantidade(-10)
    fatura.set_preco_por_item(-20.0)

    print(f"QUANTIDADE CONFIGURADA: {fatura.get_quantidade()}")
    print(f"PREÇO CONFIGURADO: R$ {fatura.get_preco_por_item():.2f}")
    print(f"VALOR AJUSTADO DA FATURA: R$ {fatura.calcular_fatura():.2f}")

main()
