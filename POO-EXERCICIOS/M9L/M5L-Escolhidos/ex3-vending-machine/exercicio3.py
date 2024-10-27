# Crie uma classe chamada VendingMachine que simule uma máquina de venda de
# produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
# compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.

class VendingMachine:
    def __init__(self):
        self.estoque = {}
        self.saldo = 0.0

    def cadastrar_produto(self, nome, preco, quantidade):
        if nome in self.estoque:
            self.estoque[nome]['quantidade'] += quantidade
        else:
            self.estoque[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto {nome} cadastrado com sucesso!")

    def selecionar_produto(self, nome):
        if nome not in self.estoque:
            print(f"Produto {nome} não disponível.")
            return None
        produto = self.estoque[nome]
        if produto['quantidade'] <= 0:
            print(f"Produto {nome} esgotado.")
            return None
        return produto

    def inserir_dinheiro(self, valor):
        if valor <= 0:
            print("Valor inválido. O valor deve ser positivo.")
            return
        self.saldo += valor
        print(f"R$ {valor:.2f} inserido. Saldo atual: R$ {self.saldo:.2f}")

    def comprar_produto(self, nome):
        produto = self.selecionar_produto(nome)
        if produto is None:
            return
        
        if self.saldo < produto['preco']:
            print(f"Saldo insuficiente. O preço do produto é R$ {produto['preco']:.2f}.")
            return
        
        self.saldo -= produto['preco']
        produto['quantidade'] -= 1
        print(f"Compra realizada com sucesso! Você comprou: {nome}. Troco: R$ {self.saldo:.2f}")
        self.saldo = 0  

    def retornar_troco(self):
        if self.saldo > 0:
            print(f"Retornando troco: R$ {self.saldo:.2f}")
            self.saldo = 0
        else:
            print("Não há troco a ser retornado.")

    def exibir_estoque(self):
        if not self.estoque:
            print("Estoque vazio.")
            return
        print("Estoque disponível:")
        for nome, info in self.estoque.items():
            print(f"{nome}: R$ {info['preco']:.2f} - Quantidade: {info['quantidade']}")

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
            vm.cadastrar_produto(nome, preco, quantidade)

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
