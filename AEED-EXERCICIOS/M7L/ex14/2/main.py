'''
Utilizando o grafo a seguir, faça um programa que crie uma árvore geradora para cada item abaixo:

a. Partida da construção da árvore pelo vértice i e realizando a escolha dos demais vértices como se executasse uma busca em largura. Ao visitar os vizinhos de um nó, siga a ordem alfabética.
b. Partida da construção da árvore pelo vértice a e realizando a escolha dos demais vértices como se executasse uma busca em profundidade. Ao visitar os vizinhos de um nó, siga a ordem alfabética.
'''

from Graph import Graph

def create_graph():
    g = Graph()
    edges = [
        ('A', 'B'), ('A', 'E'),
        ('B', 'F'),
        ('C', 'D'), ('C', 'F'), ('C', 'G'), ('C', 'H'),
        ('D', 'G'), ('D', 'H'),
        ('E', 'F'), ('E', 'I'),
        ('F', 'G'), ('F', 'I'), ('F', 'J'),
        ('G', 'H'), ('G', 'K'), ('G', 'L'),
        ('H', 'L'),
        ('J', 'K'),
        ('K', 'L')
    ]
    
    for u, v in edges:
        g.addEdge(u, v)
    
    return g

if __name__ == "__main__":
    g = create_graph()
    dfs_tree = g.DFS('A')
    print("Árvore Geradora utilizando DFS (a partir do vértice 'A'):")
    for edge in dfs_tree:
        print(edge)

'''
Objetivo: Construir uma árvore geradora mínima (MST) partindo do vértice A e utilizando a busca em profundidade.

Explicação:
Criação do Grafo:

Semelhante à BFS, o grafo é representado como uma lista de adjacência usando defaultdict.

A função addEdge adiciona uma aresta entre dois vértices, garantindo que o grafo seja não-direcionado.

Implementação da DFS:

Inicialização:

Cria um conjunto visited para rastrear se um vértice foi visitado.

Define a função DFSUtil que realiza a busca em profundidade recursivamente.

Processamento:

Na função DFS, chama a função auxiliar DFSUtil para iniciar a busca em profundidade a partir do vértice inicial (start).

A função DFSUtil marca o vértice atual como visitado, visita seus vizinhos em ordem alfabética e, para cada vizinho não visitado, adiciona a aresta na árvore geradora (tree) e chama recursivamente DFSUtil no vizinho.

Retorno:

Retorna a lista de arestas que compõem a árvore geradora mínima.
'''