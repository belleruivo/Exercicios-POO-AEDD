from person import*

def main():
    pessoa_fisica = PhysicalPerson("João Silva", "Rua A, 123", 5000, "123.456.789-00")
    pessoa_juridica = LegalPerson("Tech Solutions", "Av. B, 456", 10000, "987.654.321/0001-99", "Tech Solutions LTDA", "Soluções em TI")

    print("-="*50)
    print("PESSOA FÍSICA:")
    print(f"{pessoa_fisica.name} - CPF: {pessoa_fisica.cpf}")
    print(f"Endereço: {pessoa_fisica.address}")
    print(f"Pagamento inicial: R${pessoa_fisica.payment}")
    print(f"Pagamento após imposto (Pessoa Física): R${pessoa_fisica.doPayment()}")


    print("-="*50)
    print("PESSOA JURÍDICA:")
    print(f"{pessoa_juridica.name} - CNPJ: {pessoa_juridica.cpf}")
    print(f"Nome Fantasia: {pessoa_juridica.fantasyName}")
    print(f"Razão Social: {pessoa_juridica.socialReason}")
    print(f"Endereço: {pessoa_juridica.address}")
    print(f"Pagamento inicial: R${pessoa_juridica.payment}")
    print(f"Pagamento após imposto (Pessoa Jurídica): R${pessoa_juridica.doPayment()}")
    print("-="*50)
main()