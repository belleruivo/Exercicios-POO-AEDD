# Crie uma classe chamada VendingMachine que simule uma máquina de venda de
# produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
# compra, inserir dinheiro, retornar o troco e exibir o estoque disponíveis

from vendingMachine import VendingMachine
from cliente import Cliente
from fornecedor import Fornecedor

def main():
    vm = VendingMachine()

    while True:
        print("\nMENU:")
        print("1. Cadastrar fornecedor")
        print("2. Fornecer produto")
        print("3. Cadastrar cliente")
        print("4. Exibir estoque")
        print("5. Inserir dinheiro")
        print("6. Comprar produto")
        print("7. Exibir histórico de compras")
        print("8. Retornar troco")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_fornecedor = input("Nome do fornecedor: ")
            cnpj = input("CNPJ do fornecedor: ")
            fornecedor = Fornecedor(nome_fornecedor, cnpj)
            print(f"Fornecedor {fornecedor.nome} cadastrado com sucesso!")

        elif opcao == "2":
            nome_produto = input("Nome do produto: ")
            preco = float(input("Preço do produto: R$ "))
            quantidade = int(input("Quantidade do produto: "))
            if 'fornecedor' in locals():
                fornecedor.fornecer_produto(nome_produto, preco, quantidade, vm)
            else:
                print("Nenhum fornecedor cadastrado.")

        elif opcao == "3":
            nome_cliente = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            cliente = Cliente(nome_cliente, cpf)
            print(f"Cliente {cliente.nome} cadastrado com sucesso!")

        elif opcao == "4":
            vm.exibir_estoque()

        elif opcao == "5":
            valor = float(input("Insira o valor a ser inserido: R$ "))
            vm.inserir_dinheiro(valor)

        elif opcao == "6":
            if 'cliente' in locals():
                nome_produto = input("Nome do produto a ser comprado: ")
                cliente.comprar_produto(vm, nome_produto)
            else:
                print("Nenhum cliente cadastrado.")

        elif opcao == "7":
            if 'cliente' in locals():
                cliente.exibir_historico_compras()
            else:
                print("Nenhum cliente cadastrado.")

        elif opcao == "8":
            vm.retornar_troco()

        elif opcao == "9":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

main()

