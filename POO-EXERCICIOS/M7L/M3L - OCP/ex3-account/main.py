# Crie uma classe Account que representa uma conta bancária. A classe deve fornecer
# um método chamado debito para retirar dinheiro da conta. Assegure que a quantia de
# débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado
# inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito
# excedeu o saldo da conta”. Teste a classe implementada e seus métodos.

from poupanca import Poupanca
from conta import Conta

def main():
    tipo_conta = input("Escolha o tipo da conta (comum/poupança): ").strip().lower()
    saldo_inicial = float(input("Insira o saldo inicial da conta: R$ "))
    
    if tipo_conta == "poupança":
        conta = Poupanca(saldo_inicial)
    else:
        conta = Conta(saldo_inicial)

    print(f"Conta criada com saldo inicial: R${conta.get_saldo():.2f}")

    while True:
        print("\n1. Realizar débito")
        print("2. Ver saldo")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Insira o valor para débito: R$ "))
            conta.debito(valor)

        elif opcao == "2":
            print(f"Saldo atual: R${conta.get_saldo():.2f}")

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

main()
