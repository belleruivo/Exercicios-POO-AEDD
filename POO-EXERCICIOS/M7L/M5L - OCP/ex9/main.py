'''9. Crie uma classe chamada Invoice que possa ser utilizado por uma loja de
suprimentos de informática para representar uma fatura de um item vendido na loja.
Uma fatura deve incluir as seguintes informações como atributos:
• o número do item faturado,
• a descrição do item,
• a quantidade comprada do item e
• o preço unitário do item.
Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade
não for positiva, ela deve ser configurada como 0. Se o preço por item não for
positivo ele deve ser configurado como 0.0. Forneça um método set e um método get
para cada variável de instância. Além disso, forneça um método chamado que calcula
o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna
o valor real. Escreva um aplicativo de teste que demonstra as capacidades da classe
Invoice.'''

from faturas import *

def main():
    faturas = []

    print("-=" * 30)
    while True:
        numero_item = Fatura.obter_entrada("Digite o número do item: ", tipo=int)

        while True: 
            descricao = input("Digite a descrição do item: ")
            if descricao.replace(" ", "").isalpha():
                break
            print("Descrição inválida. Certifique-se de inserir somente letras.\n")

        quantidade = Fatura.obter_entrada("Digite a quantidade comprada: ", tipo=int)
        preco_unitario = Fatura.obter_entrada("Digite o preço unitário: ")

        fatura = Fatura(numero_item, descricao, quantidade, preco_unitario)
        faturas.append(fatura)

        continuar = input("\nDeseja adicionar outro produto? (s/n): ").strip().lower()
        print()
        if continuar != 's':
            break

    taxa_imposto = Fatura.obter_entrada("Digite a taxa de imposto padrão (%): ")

    total_sem_imposto = 0
    total_com_imposto = 0

    print("\nDetalhes da fatura:")
    for fatura in faturas:
        print(f"\nNúmero do item: {fatura.numero_item}")
        print(f"Descrição do item: {fatura.descricao}")
        print(f"Quantidade comprada: {fatura.quantidade}")
        print(f"Preço unitário: {fatura.preco_unitario:.2f}")
        valor_fatura = fatura.calcular_valor_fatura()
        print(f"Valor total vendido: {valor_fatura:.2f}")

        fatura_com_imposto = FaturaComImposto(fatura, taxa_imposto)
        valor_com_imposto = fatura_com_imposto.calcular_valor_fatura_com_imposto()

        total_sem_imposto += valor_fatura
        total_com_imposto += valor_com_imposto

    print(f"\nTotal fatura sem imposto: {total_sem_imposto:.2f}")
    print(f"Total fatura com imposto: {total_com_imposto:.2f}")
    print("-=" * 30)


if __name__ == "__main__":
    main()