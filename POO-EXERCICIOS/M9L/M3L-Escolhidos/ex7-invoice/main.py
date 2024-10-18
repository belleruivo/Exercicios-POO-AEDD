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

from cliente import Cliente
from pedido import Pedido
from fatura import Fatura

print("-" * 45)
print("         LOJA DE INFORMÁTICA")
print("-" * 45)

def main():
    nome_cliente = input("Digite o nome do cliente: ")
    cpf_cliente = input("Digite o CPF do cliente: ")
    cliente = Cliente(nome_cliente, cpf_cliente)

    num_pedidos = int(input("\nDigite o número de pedidos do cliente: "))
    for i in range(num_pedidos):
        num_pedido = input(f"\nDigite o número do pedido {i + 1}: ")
        pedido = Pedido(num_pedido)

        num_faturas = int(input(f"Digite o número de faturas para o pedido {num_pedido}: "))
        for j in range(num_faturas):
            num_fatura = input(f"Digite o número da fatura {j + 1}: ")
            descricao = input("Digite a descrição do item: ")
            quantidade = int(input("Digite a quantidade: "))
            preco_item = float(input("Digite o preço por item: "))
            
            fatura = Fatura(num_fatura, descricao, quantidade, preco_item)
            pedido.adicionar_fatura(fatura)

        cliente.adicionar_pedido(pedido)

    cliente.exibir_pedidos()

    for pedido in cliente.pedidos:
        pedido.exibir_detalhes_pedido()

main()
