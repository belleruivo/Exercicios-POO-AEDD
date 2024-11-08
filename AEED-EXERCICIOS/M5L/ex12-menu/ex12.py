# Faça um programa que apresente o menu de opções abaixo:
# MENU
# 1- Cadastrar tipo
# 2- Cadastrar produto
# 3- Consultar o preço de um produto
# 4- Excluir tipo
# 5- Sair
# Observações:
# a. Mostrar mensagem de opção inválida do menu. A opção 5 é a única que sai do
# programa.
# b. Para a implementação do programa acima, é necessário utilizar duas filas.
# c. Na primeira fila serão armazenados os tipos de produtos com seus respectivos
# percentuais de impostos. Verifique que todos os tipos sejam diferentes e cada
# tipo é identificado com apenas uma letra.
# d. Na segunda fila serão armazenados os produtos cujo número deve ser gerado
# automaticamente. O preço e o tipo devem ser digitados. Lembrando que um
# produto só pode ser cadastrado se for de um tipo também já cadastrado. Faça
# essa verificação.
# e. Na primeira opção do menu serão cadastrados os tipos, um de cada vez: cada
# vez que o usuário escolhe a opção 1 do menu, ele tem a possibilidade de
# cadastrar um novo tipo (letra que representa o tipo e percentual de imposto).
# Nesta opção, a única mensagem disponível é: Tipo cadastrado.
# f. Na segunda opção do menu serão cadastrados os produtos, um de cada vez:
# cada vez que o usuário escolhe a opção 2 do menu, ele tem a possibilidade de
# cadastrar um novo produto (número gerado automaticamente, preço e tipo
# digitados). Lembrando que um produto só pode ser cadastrado se o tipo ao
# qual ele pertence já existe na fila de tipos. Nesta opção, as mensagens
# disponíveis são: Produto cadastrado e Tipo de produto inexistente.
# g. Na terceira opção do menu, o usuário digita o número do produto que deseja
# consultar o preço e, se este existir na fila de produtos, o programa deve
# procurar por seu percentual de imposto, de acordo com o tipo do produto na
# fila de tipos, calcular e mostrar seu preço, ou seja, preço cadastrado menos o
# percentual de imposto. Nesta opção, as mensagens disponíveis são: Preço =
# valor calculado, Produto não cadastrado e Fila vazia.
# h. Na quarta opção, o programa deve excluir um tipo da fila de tipos, respeitando
# a forma de organização de uma fila. Lembrando que um tipo só pode ser
# excluído se não existir nenhum produto cadastrado para ele.

from  fila import Fila
from produto import Produto
from tipoProduto import TipoProduto

def menu():
    print("\nMENU")
    print("1- Cadastrar tipo")
    print("2- Cadastrar produto")
    print("3- Consultar o preço de um produto")
    print("4- Excluir tipo")
    print("5- Sair")

def cadastrar_tipo(fila_tipos):
    tipo = input("Digite o tipo do produto (uma letra): ").upper()
    imposto = float(input(f"Digite o percentual de imposto para o tipo {tipo}: "))
    
    for tipo_existente in fila_tipos.elementos():
        if tipo_existente.tipo == tipo:
            print("Tipo já cadastrado!")
            return
    
    novo_tipo = TipoProduto(tipo, imposto)
    fila_tipos.inserir(novo_tipo)
    print("Tipo cadastrado.")

def cadastrar_produto(fila_tipos, fila_produtos, numero_produto):
    tipo_produto = input("Digite o tipo do produto: ").upper()
    
    # Verifica se o tipo existe
    tipo_encontrado = None
    for tipo in fila_tipos.elementos():
        if tipo.tipo == tipo_produto:
            tipo_encontrado = tipo
            break

    if tipo_encontrado:
        preco = float(input(f"Digite o preço do produto {numero_produto}: "))
        produto = Produto(numero_produto, preco, tipo_produto)
        fila_produtos.inserir(produto)
        print("Produto cadastrado.")
    else:
        print("Tipo de produto inexistente.")

def consultar_preco(fila_produtos, fila_tipos):
    if fila_produtos.esta_vazia():
        print("Fila vazia.")
        return
    
    numero_produto = int(input("Digite o número do produto que deseja consultar: "))
    
    produto_encontrado = None
    for produto in fila_produtos.elementos():
        if produto.numero == numero_produto:
            produto_encontrado = produto
            break
    
    if produto_encontrado:
        tipo_produto = produto_encontrado.tipo
        tipo_encontrado = None
        for tipo in fila_tipos.elementos():
            if tipo.tipo == tipo_produto:
                tipo_encontrado = tipo
                break
        
        if tipo_encontrado:
            preco_final = produto_encontrado.preco * (1 - tipo_encontrado.percentual_imposto / 100)
            print(f"Preço = {preco_final:.2f}")
        else:
            print("Tipo de produto não encontrado.")
    else:
        print("Produto não cadastrado.")

def excluir_tipo(fila_tipos, fila_produtos):
    if fila_tipos.esta_vazia():
        print("Não há tipos cadastrados.")
        return
    
    tipo_excluir = input("Digite o tipo que deseja excluir: ").upper()
    
    tipo_encontrado = None
    for tipo in fila_tipos.elementos():
        if tipo.tipo == tipo_excluir:
            tipo_encontrado = tipo
            break
    
    if tipo_encontrado:
        # Verifica se existem produtos com o tipo para impedir a exclusão
        for produto in fila_produtos.elementos():
            if produto.tipo == tipo_excluir:
                print("Não é possível excluir este tipo porque existem produtos cadastrados com esse tipo.")
                return
        
        # Se não houver produtos para o tipo, pode excluir
        fila_tipos.remover()  # Remove o tipo
        print("Tipo excluído.")
    else:
        print("Tipo não encontrado.")

def main():
    fila_tipos = Fila()  # Fila de tipos de produtos
    fila_produtos = Fila()  # Fila de produtos
    
    numero_produto = 1  # Início dos números dos produtos
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_tipo(fila_tipos)
        elif opcao == "2":
            cadastrar_produto(fila_tipos, fila_produtos, numero_produto)
            numero_produto += 1
        elif opcao == "3":
            consultar_preco(fila_produtos, fila_tipos)
        elif opcao == "4":
            excluir_tipo(fila_tipos, fila_produtos)
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
