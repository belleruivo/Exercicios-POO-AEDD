from Graph import Graph

def create_graph():
    g = Graph()
    edges = [
        ('A', 'B'), ('A', 'E'), ('A', 'F'),
        ('B', 'C'), ('B', 'E'),
        ('C', 'D'),
        ('E', 'D'), ('E', 'G'),
        ('F', 'E'), ('F', 'H'),
        ('G', 'C'), ('G', 'H'),
        ('H', 'D')
    ]
    
    for u, v in edges:
        g.addEdge(u, v)
    
    return g

if __name__ == "__main__":
    g = create_graph()
    print("DFS starting from vertex A:")
    g.DFS('A')


'''
A classe Graph representa um grafo utilizando uma lista de adjacência.

O método addEdge adiciona uma aresta entre dois vértices.

O método DFSUtil realiza a busca em profundidade a partir de um vértice específico, utilizando recursão.

O método DFS inicializa a busca em profundidade.

O arquivo main.py cria o grafo usando os vértices e arestas fornecidos e executa a DFS a partir do vértice A.

Quando você executar o código, a saída será a ordem de visita dos vértices na busca em profundidade iniciando no vértice A.
'''