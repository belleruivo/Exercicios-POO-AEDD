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
    produtos = [] #lista vazia 
    for _ in range(n): #loop for que itera n vezes. o _ é uma variável que não será usada
        codigo = input("Digite o código do produto: ")
        descricao = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        produtos.append(Produto(codigo, descricao, preco))
    return produtos

def ordenar_produtos(produtos): #implementa o algoritmo de ordenação por inserção
    for i in range(1, len(produtos)): # dentro do intervalo de 1 até o tamanho da lista de produtos
        key = produtos[i] # key é o produto na posição i
        j = i - 1 # j é o produto na posição anterior a i
        while j >= 0 and key.codigo < produtos[j].codigo:
            produtos[j + 1] = produtos[j] # desloque o produto na posição j para a direita
            j -= 1 # decrementa j para verificar o próximo produto
        produtos[j + 1] = key # insere o produto key na posição j + 1

def busca_sequencial(produtos, codigo):
    comparacoes = 0
    for produto in produtos:
        comparacoes += 1
        if produto.codigo == codigo:
            return produto, comparacoes
    return None, comparacoes

def busca_binaria(produtos, codigo):
    comparacoes = 0
    esquerda, direita = 0, len(produtos) - 1
    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        if produtos[meio].codigo == codigo:
            return produtos[meio], comparacoes
        elif produtos[meio].codigo < codigo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None, comparacoes

def main():
    n = int(input("Quantos produtos deseja cadastrar? "))
    produtos = cadastrar_produtos(n)
    ordenar_produtos(produtos)
    
    codigo_busca = input("Digite o código do produto a ser buscado: ")
    
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

if __name__ == "__main__":
    main()