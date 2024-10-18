from Produto import Produto
from Cliente import Cliente
from Fatura import Fatura

print("-" * 30)
print("     LOJA DE INFORMÁTICA")
print("-" * 30)

def main():
    nome_cliente = input("Digite o nome do cliente: ")
    endereco_cliente = input("Digite o endereço do cliente: ")
    cliente = Cliente(nome_cliente, endereco_cliente)

    descricao_produto = input("Digite a descrição do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$"))
    produto = Produto(descricao_produto, preco_produto)

    numFatura = input("Digite o número da fatura: ")
    quantidade = int(input("Digite a quantidade comprada: "))
    fatura = Fatura(numFatura, cliente, produto, quantidade)

    print("-" * 30)
    print("           FATURA")
    print("-" * 30)
    print("\nNúmero da fatura: {}".format(fatura.get_numFatura()))
    print("Cliente: {}".format(fatura.get_cliente()))
    print("Produto: {}".format(fatura.get_produto()))
    print("Quantidade: {}".format(fatura.get_quantidade()))
    print("Valor total da fatura: R$ {:.2f}".format(fatura.calcular_fatura()))

main()
