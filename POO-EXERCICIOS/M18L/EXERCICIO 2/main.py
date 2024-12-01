'''
Implemente as classes descritas no diagrama abaixo, considerando que:
a. Um pedido é composto por um conjunto de itens pedidos.
b. Um item pedido associa-se com um produto.
c. O cálculo do valor total do pedido deverá ser feito mediante a soma do preço de cada produto incluído nos itens pedidos.
'''

from product import Product
from item_order import ItemOrder
from order import Order

def adicionar_produto():
    code = int(input("Digite o código do produto: "))
    value = float(input("Digite o valor do produto: "))
    description = input("Digite a descrição do produto: ")
    return Product(code, value, description)

def adicionar_item(pedido, produtos):
    code = int(input("Digite o código do produto que deseja adicionar ao pedido: "))
    product = next((p for p in produtos if p.code == code), None)
    if product:
        quantidade = int(input(f"Digite a quantidade do produto {product.description}: "))
        item = ItemOrder(product, quantidade)
        pedido.addItem(item)
        print(f'Item adicionado: {quantidade}x {product.description}')
    else:
        print("Produto não encontrado!")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    for produto in produtos:
        print(f'Código: {produto.code}, Descrição: {produto.description}, Valor: {produto.value}')

def listar_pedido(pedido):
    if not pedido.items:
        print("Nenhum item no pedido.")
        return
    
    for item in pedido.items:
        print(f'Produto: {item.product.description}, Quantidade: {item.quantify}, Total: {item.get_total()}')
    print(f'Total do Pedido: {pedido.getTotal()}')

def main():
    produtos = []
    pedido = Order()
    
    while True:
        print("\nSistema de Gestão de Pedidos")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Adicionar Item ao Pedido")
        print("4. Listar Pedido")
        print("5. Sair")
        
        opcao = int(input("Selecione uma opção (1-5): "))
        
        if opcao == 1:
            produto = adicionar_produto()
            produtos.append(produto)
            print("Produto adicionado com sucesso!")
        elif opcao == 2:
            listar_produtos(produtos)
        elif opcao == 3:
            adicionar_item(pedido, produtos)
        elif opcao == 4:
            listar_pedido(pedido)
        elif opcao == 5:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

