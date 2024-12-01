from person import *

def main():
    print("1 - Pessoa Física")
    print("2 - Pessoa Jurídica")
    while True:
        try:
            opcao = int(input("Escolha o tipo de pessoa (1 ou 2): "))
            if opcao not in [1, 2]:
                raise ValueError("Opção inválida!")
            break
        except ValueError as e:
            print(f"Insira um número válido")

    nome = input("\nNome: ")
    endereco = input("Endereço: ")

    while True:
        try:
            pagamento_inicial = float(input("Pagamento inicial: "))
            break
        except ValueError:
            print("Certifique-se de inserir um número válido.")

    if opcao == 1:
        while True:
            cpf = input("CPF: ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            print("Certifique-se de inserir um CPF válido (11 dígitos).")

        pessoa_fisica = PhysicalPerson(nome, endereco, pagamento_inicial, cpf)

        print("-=" * 50)
        print("PESSOA FÍSICA:")
        print(f"{pessoa_fisica.name} - CPF: {pessoa_fisica.cpf}")
        print(f"Endereço: {pessoa_fisica.address}")
        print(f"Pagamento inicial: R${pessoa_fisica.payment:.2f}")
        print(f"Pagamento após imposto: R${pessoa_fisica.doPayment():.2f}")
        print("-=" * 50)

    else:
        while True:
            cnpj = input("CNPJ: ")
            if len(cnpj) == 14 and cnpj.isdigit():
                break
            print("Certifique-se de inserir um CNPJ válido (14 dígitos).")

        nome_fantasia = input("Nome Fantasia: ")
        razao_social = input("Razão Social: ")

        pessoa_juridica = LegalPerson(nome, endereco, pagamento_inicial, cnpj, nome_fantasia, razao_social)

        print("-=" * 50)
        print("PESSOA JURÍDICA:")
        print(f"{pessoa_juridica.name} - CNPJ: {pessoa_juridica.cpf}")
        print(f"Nome Fantasia: {pessoa_juridica.fantasyName}")
        print(f"Razão Social: {pessoa_juridica.socialReason}")
        print(f"Endereço: {pessoa_juridica.address}")
        print(f"Pagamento inicial: R${pessoa_juridica.payment:.2f}")
        print(f"Pagamento após imposto: R${pessoa_juridica.doPayment():.2f}")
        print("-=" * 50)

if __name__ == "__main__":
    main()
