from veiculos import Carro, Moto, Caminhao
from cliente import Cliente

def main():
    lista_veiculos = []  
    lista_clientes = []

    while True:
        print("\n=== Sistema de Concessionária ===")
        print("1. Registrar veículo")
        print("2. Registrar cliente")
        print("3. Vender veículo")
        print("4. Sair")
        
        while True:
            opcao = input("Escolha uma opção: ").strip()
            if opcao not in {"1", "2", "3", "4"}:
                print("Opção inválida! Tente novamente.\n")
            else:
                break
        
        if opcao == "1":
            print("\nEscolha o tipo de veículo:")
            print("1. Carro")
            print("2. Moto")
            print("3. Caminhão\n")

            while True:
                tipo = input("Digite o número correspondente ao tipo de veículo: ").strip()
                if tipo not in {"1", "2", "3"}:
                    print("Tipo inválido! Tente novamente.\n")
                else:
                    break

            while True:
                try:
                    ano = int(input("Digite o ano do veículo: "))
                    break
                except ValueError:
                    print("Certifique-se de inserir um ano válido!\n")

            marca = input("Digite a marca do veículo: ")

            while True:
                seguro = input("O veículo possui seguro? (sim/não): ").strip().lower()
                if seguro in ("sim", "não"):
                    break
                print("Entrada inválida! Responda com 'sim' ou 'não'.\n")

            if tipo == "1":
                while True:
                    try:
                        portas = int(input("Digite o número de portas do automóvel: "))
                        veiculo = Carro(ano, marca, seguro, portas)
                        lista_veiculos.append(veiculo)
                        print("Veículo registrado com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!\n")
            elif tipo == "2":
                while True:
                    try:
                        cilindradas = int(input("Digite a quantidade de cilindradas da moto: "))
                        veiculo = Moto(ano, marca, seguro, cilindradas)
                        lista_veiculos.append(veiculo)
                        print("Veículo registrado com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!\n")
            elif tipo == "3":
                while True:
                    try:
                        capacidade_carga = float(input("Digite a capacidade de carga do caminhão (em toneladas): "))
                        veiculo = Caminhao(ano, marca, seguro, capacidade_carga)
                        lista_veiculos.append(veiculo)
                        print("Veículo registrado com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!\n")

        elif opcao == "2":
            nome = input("\nDigite o nome do cliente: ")
            email = input("Digite o e-mail do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            cliente = Cliente(nome, email, telefone)
            lista_clientes.append(cliente)
            print(f"Cliente {cliente.nome} registrado com sucesso!")

        elif opcao == "3":
            if not lista_veiculos or not lista_clientes:
                print("Nenhum veículo ou cliente registrado para a venda!")
            else:
                print("\nVeículos registrados:")
                for i, veiculo in enumerate(lista_veiculos, 1):
                    print(f"{i}. {veiculo.registrar()}")
                
                print("\nClientes registrados:")
                for i, cliente in enumerate(lista_clientes, 1):
                    print(f"{i}. {cliente}")

                while True:
                    try:
                        venda_id_veiculo = int(input("\nDigite o número do veículo a ser vendido: ")) - 1
                        venda_id_cliente = int(input("\nDigite o número do cliente que está comprando: ")) - 1
                        if 0 <= venda_id_veiculo < len(lista_veiculos) and 0 <= venda_id_cliente < len(lista_clientes):
                            veiculo_vendido = lista_veiculos.pop(venda_id_veiculo) 
                            cliente_comprador = lista_clientes[venda_id_cliente]
                            cliente_comprador.adicionar_veiculo(veiculo_vendido)  
                            print(f"Veículo {veiculo_vendido.marca} vendido para {cliente_comprador.nome}.")
                            break
                        else:
                            print("ID de veículo ou cliente inválido. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida! Digite um número válido.\n")

        elif opcao == "4":
            print("\nSaindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

main()






