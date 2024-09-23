# Crie uma classe Invoice para que uma loja de suprimentos de informática possa
# utilizá-la para representar a fatura de um item vendido na loja. Uma Invoice deve
# incluir quatro variáveis de instância: o número da fatura (string), a descrição (string),
# a quantidade comprada de um item (int) e o preço por item (float). Sua classe deve ter
# um construtor que inicializa as quatro variáveis de instância.
# Forneça um método set e um get para cada variável de instância. Forneça também um método chamado que
# calcula o valor da fatura (multiplica preço por quantidade do item) e retorna o
# resultado. Se a quantidade de itens passada pelo usuário não for positiva, deve ser
# configurada como 0. Se o preço do item não for positivo, deve ser configurado como
# 0.0. Teste a classe implementada e seus métodos.

class Invoice:
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

    def get_precoItem(self):
        return self.precoItem

    def set_precoItem(self, precoItem):
        self.precoItem = precoItem if precoItem > 0 else 0.0

    def calcular_fatura(self):
        return self.quantidade * self.precoItem

def main():
    numFatura = "A123"
    descricao = "Teclado"
    quantidade = 5
    precoItem = 50.0

    fatura = Invoice(numFatura, descricao, quantidade, precoItem)

    print("Numero da fatura: {}".format(fatura.get_numFatura()))
    print("Descrição: {}".format(fatura.get_descricao()))
    print("Quantidade: {}".format(fatura.get_quantidade()))
    print("Preço por item: R$ {:.2f}".format(fatura.get_precoItem()))

    print("Valor total da fatura: R$ {}".format(fatura.calcular_fatura()))

    fatura.set_quantidade(-10)
    fatura.set_precoItem(-20.0) 

    print("Quantidade ajustada: {}".format(fatura.get_quantidade()))
    print("Preço ajustado: R$ {:.2f}".format(fatura.get_precoItem()))
    print("Valor ajustado da fatura: R$ {:.2f}".format(fatura.calcular_fatura()))

main()