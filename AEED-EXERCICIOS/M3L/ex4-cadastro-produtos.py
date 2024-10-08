'''
4. Faça um programa que cadastre n produtos. Para cada produto devem ser
cadastrados os seguintes dados: código, descrição e preço. Use um método de
ordenação e em seguida calcule e mostre quantas comparações devem ser feitas
para encontrar um funcionário pelo código:

a. Usando busca sequencial.
b. Usando busca binária.

'''

class Produto:
    def __init__(self, codigo, descricao, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco

def cadastrar_produtos(n):
    produtos = [] # lista vazia para armazenar os produtos
    codigos_existentes = set() # conjunto para armazenar os códigos já cadastrados
    for _ in range(n): # loop for que itera n vezes. o _ é uma variável que não será usada
        while True:
            try:
                codigo = input("Digite o código do produto: ").strip() #strip remove espaços em branco
                if not codigo.isdigit(): # apenas números e inteiros
                    raise ValueError("O código deve ser um número inteiro.")
                codigo = int(codigo)
                if codigo in codigos_existentes:
                    raise ValueError("Código já cadastrado. Digite um código único.")
                
                descricao = input("Digite a descrição do produto: ").strip()
                if not descricao or descricao.isdigit():
                    raise ValueError("A descrição não pode ser vazia ou um número.")
                
                preco = input("Digite o preço do produto: ").strip()
                if not preco:
                    raise ValueError("O preço não pode ser vazio.")
                preco = float(preco)
                
                produtos.append(Produto(codigo, descricao, preco)) # add novo produto à lista
                codigos_existentes.add(codigo) # add código ao conjunto de códigos existentes
                break
            except ValueError as e:
                print(e)
    return produtos

def ordenar_produtos(produtos): # implementa o algoritmo de ordenação por inserção
    for i in range(1, len(produtos)): # dentro do intervalo de 1 até o tamanho da lista de produtos
        key = produtos[i] # key é o produto na posição i
        j = i - 1 # j é o produto na posição anterior a i
        while j >= 0 and key.codigo < produtos[j].codigo: # enquanto j for maior ou igual a 0 e o código do produto key for menor que o código do produto na posição j
            produtos[j + 1] = produtos[j] # desloque o produto na posição j para a direita
            j -= 1 # decrementa j para verificar o próximo produto
        produtos[j + 1] = key # insere o produto key na posição j + 1

def busca_sequencial(produtos, codigo): 
    comparacoes = 0 # contador de comparações
    for produto in produtos: # percorre a lista de produtos
        comparacoes += 1 # incrementa o contador de comparações
        if produto.codigo == codigo: # verifica se o código do produto é igual ao código buscado
            return produto, comparacoes # retorna o produto encontrado e o número de comparações
    return None, comparacoes # retorna None e o número de comparações se o produto não for encontrado

def busca_binaria(produtos, codigo): 
    comparacoes = 0 
    esquerda, direita = 0, len(produtos) - 1 # define os limites esquerdo e direito da busca
    while esquerda <= direita: # enquanto o limite esquerdo for menor ou igual ao limite direito
        comparacoes += 1 # incrementa o contador de comparações
        meio = (esquerda + direita) // 2 # calcula o índice do meio
        if produtos[meio].codigo == codigo: # verifica se o código do produto no meio é igual ao código buscado
            return produtos[meio], comparacoes # retorna o produto encontrado e o número de comparações
        elif produtos[meio].codigo < codigo: # se o código do produto no meio for menor que o código buscado
            esquerda = meio + 1 # ajusta o limite esquerdo para o meio + 1
        else: # se o código do produto no meio for maior que o código buscado
            direita = meio - 1 # ajusta o limite direito para o meio - 1
    return None, comparacoes 

def main():
    while True:
        try:
            n = int(input("Quantos produtos deseja cadastrar? ")) 
            if n <= 0:
                print("O número de produtos deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    produtos = cadastrar_produtos(n) 
    ordenar_produtos(produtos) 
    
    while True:
        codigo_busca = input("Digite o código do produto a ser buscado: ").strip() 
        if not codigo_busca.isdigit():
            print("O código deve ser um número inteiro.")
            continue
        codigo_busca = int(codigo_busca)
        break
    
    produto, comparacoes_seq = busca_sequencial(produtos, codigo_busca) 
    if produto: 
        print(f"Produto encontrado (Busca Sequencial): {produto.descricao}, Comparações: {comparacoes_seq}")
    else: 
        print(f"Produto não encontrado (Busca Sequencial), Comparações: {comparacoes_seq}")
    
    produto, comparacoes_bin = busca_binaria(produtos, codigo_busca) 
    if produto: 
        print(f"Produto encontrado (Busca Binária): {produto.descricao}, Comparações: {comparacoes_bin}")
    else: 
        print(f"Produto não encontrado (Busca Binária), Comparações: {comparacoes_bin}")

main()