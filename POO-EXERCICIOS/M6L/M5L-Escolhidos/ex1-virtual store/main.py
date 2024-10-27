'''1. Crie uma classe chamada VirtualStore que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho
de compras, aplicar descontos e calcular o valor total da compra.'''

from virtualstore import VirtualStore
from cliente import Cliente

def main():
    loja = VirtualStore()
    print("-=" * 30)

    while True:
        print("Menu:")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Mostrar Produtos")
        print("4. Adicionar ao Carrinho")
        print("5. Mostrar Carrinho")
        print("6. Aplicar Desconto")
        print("7. Finalizar Compra")
        print("8. Sair")

        escolha = input("\nEscolha uma opção: ")
        print()


        if escolha == '1':
            while True:
                nome_cliente = input("Digite o nome do cliente: ").lower()
                if nome_cliente.replace(" ", "").isalpha():
                    break
                print("Nome inválido. Certifique-se de inserir somente letras.\n")
            email_cliente = loja.obter_email()

            if loja.cliente_existe(nome_cliente, email_cliente):
                print(f"Cliente '{nome_cliente}' já está cadastrado!\n")
            else:
                cliente = Cliente(nome_cliente, email_cliente)
                loja.clientes.append(cliente)

                print(f"Cliente '{cliente.nome}' cadastrado com sucesso!\n")

        elif escolha == '2':
            loja.adicionar_produto()
        elif escolha == '3':
            loja.mostrar_produtos()
        elif escolha == '4':
            cliente = loja.selecionar_cliente()
            if cliente:
                loja.adicionar_ao_carrinho(cliente)
        elif escolha == '5':
            cliente = loja.selecionar_cliente()
            if cliente:
                cliente.mostrar_carrinho()
        elif escolha == '6':
            cliente = loja.selecionar_cliente()
            if cliente:
                loja.aplicar_desconto(cliente)
        elif escolha == '7':
            cliente = loja.selecionar_cliente()
            if cliente:
                loja.finalizar_compra(cliente)
        elif escolha == '8':
            print("Saindo da loja. Obrigado!")
            print("-=" * 30)
            break
        else:
            print("Opção inválida! Tente novamente.\n")


main()