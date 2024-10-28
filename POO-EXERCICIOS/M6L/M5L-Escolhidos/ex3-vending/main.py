from produto import Produto
from transacao import Transacao
from vendingMachine import VendingMachine

def main():
    vm = VendingMachine()
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Exibir Estoque")
        print("3. Inserir Dinheiro")
        print("4. Comprar Produto")
        print("5. Retornar Troco")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade disponível: "))
            vm.cadastrar_produto(nome, preco, quantidade)

        elif opcao == "2":
            vm.exibir_estoque()

        elif opcao == "3":
            valor = float(input("Quanto você quer inserir (R$): "))
            vm.inserir_dinheiro(valor)

        elif opcao == "4":
            nome_produto = input("Nome do produto para comprar: ")
            vm.comprar_produto(nome_produto)

        elif opcao == "5":
            vm.retornar_troco()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

main()  
