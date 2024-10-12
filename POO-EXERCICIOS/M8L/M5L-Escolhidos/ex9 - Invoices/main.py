from invoice import Invoice  # Importa a classe Invoice
from input_manager import InputManager  # Importa a classe InputManager

def main():
    faturas = []  
    total_faturas = 0

    print("-="*30)
    while True:
        numero_item = InputManager.obter_entrada("Digite o número do item: ", tipo=int)
        descricao = input("Digite a descrição do item: ")
        quantidade = InputManager.obter_entrada("Digite a quantidade comprada: ", tipo=int)
        preco_unitario = InputManager.obter_entrada("Digite o preço unitário: ")

        # Criação da fatura com injeção de dependência
        fatura = Invoice(numero_item, descricao, quantidade, preco_unitario)
        faturas.append(fatura)  

        total_faturas += fatura.calcular_valor_fatura()

        continuar = input("\nDeseja adicionar outro produto? (s/n): ").strip().lower()
        print()
        if continuar != 's':
            break

    # Exibindo detalhes das faturas
    print("\nDetalhes das faturas:")
    for fatura in faturas:
        print(f"\nNúmero do item: {fatura.numero_item}")
        print(f"Descrição do item: {fatura.descricao}")
        print(f"Quantidade comprada: {fatura.quantidade}")
        print(f"Preço unitário: {fatura.preco_unitario:.2f}")
        print(f"Valor total da fatura: {fatura.calcular_valor_fatura():.2f}")

    print(f"\nTotal de todas as faturas: {total_faturas:.2f}")
    print("-="*30)

if __name__ == "__main__":
    main()  # Chama a função main
