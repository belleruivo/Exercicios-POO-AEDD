from store import Store

def main():
    loja = Store()  # Criar uma instância da loja

    while True:
        numero_item = Store.obter_entrada("Digite o número do item: ", tipo=int)
        descricao = input("Digite a descrição do item: ")
        quantidade = Store.obter_entrada("Digite a quantidade comprada: ", tipo=int)
        preco_unitario = Store.obter_entrada("Digite o preço unitário: ")

        loja.adicionar_fatura(numero_item, descricao, quantidade, preco_unitario)

        continuar = input("\nDeseja adicionar outro produto? (s/n): ").strip().lower()
        if continuar != 's':
            break

    loja.exibir_faturas()  # Exibir as faturas
    print(f"\nTotal de todas as faturas: R${loja.calcular_total_faturas():.2f}")

if __name__ == "__main__":
    main()
