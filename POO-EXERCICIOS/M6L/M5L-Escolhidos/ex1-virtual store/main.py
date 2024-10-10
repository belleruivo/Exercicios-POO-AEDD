from virtualstore import VirtualStore

def main():
    loja = VirtualStore()
    print("-=" * 30)

    while True:
        print("Menu:")
        print("1. Cadastrar Produto")
        print("2. Mostrar Produtos")
        print("3. Adicionar ao Carrinho")
        print("4. Aplicar Desconto")
        print("5. Finalizar Compra")
        print("6. Sair")

        escolha = input("\nEscolha uma opção: ")
        print()

        if escolha == '1':
            loja.adicionar_produto()
        elif escolha == '2':
            loja.mostrar_produtos()
        elif escolha == '3':
            loja.adicionar_ao_carrinho()
        elif escolha == '4':
            loja.aplicar_desconto()
        elif escolha == '5':
            loja.finalizar_compra()
        elif escolha == '6':
            print("Saindo da loja. Obrigado!")
            print("-=" * 30)
            break
        else:
            print("Opção inválida! Tente novamente.\n")


main()