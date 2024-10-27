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
#Adicionar input

from cliente import Cliente
from produto import Produto
from invoice import Invoice
from impostoSimples import ImpostoSimples
from pagamentoCartaoCredito import PagamentoCartaoCredito
from faturamento import Faturamento


def main():
    # Criação de produtos e cliente
    cliente = Cliente("João Silva", "123.456.789-00")
    produto1 = Produto(1, "Mouse", 50.0)
    produto2 = Produto(2, "Teclado", 100.0)

    itens = [(produto1, 2), (produto2, 1)]  # Comprou 2 mouses e 1 teclado
    fatura = Invoice("001", cliente, itens)

    imposto = ImpostoSimples()
    pagamento = PagamentoCartaoCredito() 

    faturamento = Faturamento(imposto, pagamento)
    faturamento.processar_fatura(fatura)

main()
