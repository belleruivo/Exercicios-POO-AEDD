'''1. Crie uma classe chamada VirtualStore que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho
de compras, aplicar descontos e calcular o valor total da compra.'''

from virtualStore import VirtualStore
from carrinho import Cart
from descontos import Discount

def obter_entrada(mensagem, tipo=str, positivo=False):
    while True:
        try:
            entrada = input(mensagem).replace(',', '.')
            entrada = tipo(entrada)
            if positivo and entrada < 0:
                raise ValueError("O valor não pode ser negativo.")
            return entrada
        except ValueError:
            print(f"Entrada inválida. Tente novamente.\n")

def main():
    loja = VirtualStore()
    carrinho = Cart()
    print("-=" * 30)

    while True:
        print("Menu:")
        print("1. Cadastrar Produto")
        print("2. Mostrar Produtos")
        print("3. Adicionar ao Carrinho")
        print("4. Aplicar Desconto")
        print("5. Finalizar Compra")
        print("6. Sair")

        escolha = input("\nEscolha uma opção: ")
        print()

        if escolha == '1':
            nome = input("Digite o nome do produto: ")
            preco = obter_entrada("Digite o preço do produto: R$ ", tipo=float, positivo=True)
            loja.adicionar_produto(nome, preco)
        elif escolha == '2':
            loja.mostrar_produtos()
        elif escolha == '3':
            nome_produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
            produto = loja.buscar_produto(nome_produto)
            if produto:
                carrinho.adicionar_produto(produto)
                print(f"Produto '{produto.nome}' adicionado ao carrinho!\n")
            else:
                print(f"Produto '{nome_produto}' não encontrado.\n")
        elif escolha == '4':
            tipo_desconto = input("Digite o tipo de desconto (percentual/fixo): ").lower()
            if tipo_desconto not in ["percentual", "fixo"]:
                print("Tipo de desconto inválido! Tente novamente.\n")
                continue

            valor_desconto = obter_entrada(
                f"Digite o valor do desconto {'(%)' if tipo_desconto in ['percentual'] else '(R$)'}: ", 
                tipo=float, positivo=True
            )
            desconto = Discount(tipo_desconto, valor_desconto)
            carrinho.definir_desconto(desconto)
        elif escolha == '5':
            carrinho.mostrar_carrinho()
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total:.2f}\n")
        elif escolha == '6':
            print("Saindo da loja. Obrigado!")
            print("-=" * 30)
            break
        else:
            print("Opção inválida! Tente novamente.\n")
            
main()
