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
            nome = input("Digite o nome do funcionário: ")
            sobrenome = input("Digite o sobrenome do funcionário: ")
            salario_mensal = float(input("Digite o salário mensal: "))
            payroll.add_employee(nome, sobrenome, salario_mensal)
        elif choice == '2':
            payroll.display_all_employees()
        elif choice == '3':
            porcentagem = float(input("Digite a porcentagem de aumento: "))
            payroll.give_raise_to_all(porcentagem)
        elif choice == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
