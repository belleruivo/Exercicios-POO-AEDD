from person import Person

def main():
    try:
        pessoa = Person()

        pessoa.set_nome("João Silva")
        pessoa.set_endereco("Rua das Flores, 123")
        pessoa.set_cpf("12345678901")
        pessoa.set_rg("MG1234567")
        pessoa.set_telefone("31987654321")

        print("Nome:", pessoa.get_nome())
        print("Endereço:", pessoa.get_endereco())
        print("CPF:", pessoa.get_cpf())
        print("RG:", pessoa.get_rg())
        print("Telefone:", pessoa.get_telefone())

    except ValueError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()