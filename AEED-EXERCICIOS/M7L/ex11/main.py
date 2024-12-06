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
    print("BFS starting from vertex B:")
    g.BFS('B')


'''
Neste código:

A classe Graph representa um grafo utilizando uma lista de adjacência.

O método addEdge adiciona uma aresta entre dois vértices.

O método BFS realiza a busca em largura começando no vértice especificado.

O arquivo main.py cria o grafo usando os vértices e arestas fornecidos e executa a BFS a partir do vértice B.

Quando você executar o código, a saída será a ordem de visita dos vértices na busca em largura iniciando no vértice B.
'''