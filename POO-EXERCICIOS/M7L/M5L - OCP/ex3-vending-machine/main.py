# Crie uma classe chamada VendingMachine que simule uma máquina de venda de
# produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
# compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.

#Consertar função do troco 

from vendingMachine import VendingMachine
from produto import Produto

def main():
    vm = VendingMachine()

    while True:
        print("\nMENU:")
        print("1. Cadastrar produto")
        print("2. Exibir estoque")
        print("3. Inserir dinheiro")
        print("4. Comprar produto")
        print("5. Retornar troco")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: R$ "))
            quantidade = int(input("Quantidade do produto: "))
            produto = Produto(nome, preco, quantidade)
            vm.cadastrar_produto(produto)

        elif opcao == "2":
            vm.exibir_estoque()

        elif opcao == "3":
            valor = float(input("Insira o valor a ser inserido: R$ "))
            vm.inserir_dinheiro(valor)

        elif opcao == "4":
            nome = input("Nome do produto a ser comprado: ")
            vm.comprar_produto(nome)

        elif opcao == "5":
            vm.retornar_troco()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

main()
