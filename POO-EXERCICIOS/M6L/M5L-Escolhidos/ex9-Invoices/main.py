from store import Store

def main():
    loja = Store()  # Criar uma instância da loja

    while True:
        try:
            numero_item = Store.obter_entrada("Digite o número do item: ", tipo=int)
            descricao = input("Digite a descrição do item: ")
            quantidade = Store.obter_entrada("Digite a quantidade comprada: ", tipo=int)
            preco_unitario = Store.obter_entrada("Digite o preço unitário: ", tipo=float)

            loja.adicionar_fatura(numero_item, descricao, quantidade, preco_unitario)
            print(f"\nProduto '{descricao}' adicionado com sucesso!")

        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
            continue  # Retorna ao início do loop para tentar novamente

        continuar = input("\nDeseja adicionar outro produto? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\n--- Faturas da Loja ---")
    loja.exibir_faturas()  # Exibir as faturas
    total = loja.calcular_total_faturas()
    print(f"\nTotal de todas as faturas: R${total:.2f}")

if __name__ == "__main__":
    main()
