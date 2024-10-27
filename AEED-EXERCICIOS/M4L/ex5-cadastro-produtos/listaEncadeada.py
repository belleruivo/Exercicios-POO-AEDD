from node import Node

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar_produto(self, produto):
        novo_node = Node(produto)
        if self.cabeca is None:
            self.cabeca = novo_node
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_node

    def aplicar_desconto(self, taxa_desconto):
        atual = self.cabeca
        while atual:
            desconto = atual.produto.preco * (taxa_desconto / 100)
            atual.produto.preco -= desconto
            atual = atual.proximo

    def relatorio(self):
        quantidade_acima_500 = 0
        atual = self.cabeca
        relatorio_produtos = []

        while atual:
            relatorio_produtos.append((atual.produto.codigo, atual.produto.preco))
            if atual.produto.quantidade > 500:
                quantidade_acima_500 += 1
            atual = atual.proximo

        return relatorio_produtos, quantidade_acima_500
