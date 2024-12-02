# Crie uma classe Account com um método chamado update() que atualiza a conta de
# acordo com a taxa percentual:
# class Account:
# # Bank account
# def update(self, tax):
# self._balance += self._balance * tax
# Crie duas subclasses da classe Account: CurrentAccount e SavingsAccount. Ambas
# terão o método update() reescrito: a CurrentAccount deve atualizar-se com o dobro
# da taxa e a SavingsAccount deve atualizar-se com o triplo da taxa.
class Account:
    def __init__(self, balance):
        self._balance = balance

    def update(self, tax):
        self._balance += self._balance * tax

    def get_balance(self):
        return self._balance


class CurrentAccount(Account):
    def update(self, tax):
        self._balance += self._balance * (2 * tax)


class SavingsAccount(Account):
    def update(self, tax):
        self._balance += self._balance * (3 * tax)

def main():
    print("Bem-vindo ao sistema de gerenciamento de contas bancárias!")
    print("Tipos de contas disponíveis:")
    print("1. Conta Corrente")
    print("2. Conta Poupança")
    print("3. Conta Genérica")

    while True:
        try:
            tipo_conta = int(input("\nDigite o número correspondente ao tipo de conta que deseja criar: "))
            if tipo_conta not in {1, 2, 3}:
                raise ValueError
            break
        except ValueError:
            print("Entrada inválida! Escolha entre 1, 2 e 3.")

    while True:
        try:
            saldo_inicial = float(input("Digite o saldo inicial da conta: "))
            if saldo_inicial < 0:
                raise ValueError
            break
        except ValueError:
            print("Entrada inválida! Digite um número positivo para o saldo.")

    if tipo_conta == 1:
        conta = CurrentAccount(saldo_inicial)
        tipo = "Conta Corrente"
    elif tipo_conta == 2:
        conta = SavingsAccount(saldo_inicial)
        tipo = "Conta Poupança"
    else:
        conta = Account(saldo_inicial)
        tipo = "Conta Genérica"

    print(f"\n{tipo} criada com sucesso com saldo inicial de R$ {saldo_inicial:.2f}.")

    while True:
        try:
            taxa = float(input("Digite a taxa percentual de atualização (em %): ")) / 100
            if taxa < 0:
                raise ValueError
            break
        except ValueError:
            print("Entrada inválida! Digite um número positivo para a taxa.")

    conta.update(taxa)

    print(f"O saldo atualizado da {tipo} é R$ {conta.get_balance():.2f}.")

main()

