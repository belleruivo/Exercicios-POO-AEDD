from payroll import Payroll

def main():
    payroll = Payroll()

    while True:
        print("\n--- Menu de Gestão de Funcionários ---")
        print("1. Adicionar novo funcionário")
        print("2. Exibir todos os funcionários")
        print("3. Dar aumento para todos os funcionários")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == '1':
            nome = input("Digite o nome do funcionário: ").strip().title()
            sobrenome = input("Digite o sobrenome do funcionário: ").strip().title()
            
            try:
                salario_mensal = float(input("Digite o salário mensal: "))
                if salario_mensal <= 0:
                    print("O salário deve ser um valor positivo. Tente novamente.")
                else:
                    payroll.add_employee(nome, sobrenome, salario_mensal)
                    print(f"Funcionário {nome} {sobrenome} adicionado com sucesso!")
            except ValueError:
                print("Erro: Digite um valor numérico válido para o salário.")

        elif choice == '2':
            try:
                payroll.display_all_employees()
            except Exception as e:
                print(f"Erro ao exibir funcionários: {e}")

        elif choice == '3':
            try:
                porcentagem = float(input("Digite a porcentagem de aumento: "))
                if porcentagem <= 0:
                    print("A porcentagem de aumento deve ser um valor positivo. Tente novamente.")
                else:
                    payroll.give_raise_to_all(porcentagem)
                    print(f"Aumento de {porcentagem}% aplicado a todos os funcionários.")
            except ValueError:
                print("Erro: Digite um valor numérico válido para a porcentagem.")
            except Exception as e:
                print(f"Erro ao aplicar aumento: {e}")

        elif choice == '4':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente escolhendo uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
