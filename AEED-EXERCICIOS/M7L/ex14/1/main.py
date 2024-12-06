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
    bfs_tree = g.BFS('I')
    print("Árvore Geradora utilizando BFS (a partir do vértice 'I'):")
    for edge in bfs_tree:
        print(edge)


'''
Objetivo: Construir uma árvore geradora mínima (MST) partindo do vértice I e utilizando a busca em largura.
Explicação:
Criação do Grafo:

O grafo é representado como uma lista de adjacência usando defaultdict.

A função addEdge adiciona uma aresta entre dois vértices, garantindo que o grafo seja não-direcionado.

Implementação da BFS:

Inicialização:

Cria um dicionário visited para rastrear se um vértice foi visitado.

Cria uma fila (queue) para gerenciar a ordem de visitação dos vértices.

Define o vértice inicial (start) como visitado e o adiciona à fila.

Processamento:

Enquanto a fila não estiver vazia, remove o vértice da frente da fila e visita seus vizinhos em ordem alfabética.

Para cada vizinho não visitado, marca como visitado, adiciona à fila e registra a aresta na árvore geradora (tree).

Retorno:

Retorna a lista de arestas que compõem a árvore geradora mínima.
'''