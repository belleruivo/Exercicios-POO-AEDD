'''
Seja um grafo G cujos vértices são os inteiros de 1 a 8 e os vértices adjacentes a
cada vértice são dados pela tabela abaixo:
a. Desenhe o grafo G.
b. Crie um programa que o represente por meio de uma matriz de adjacência e por
meio de uma lista de adjacência.
'''

from GraphAM import GraphAM

def create_graph():
    g = GraphAM(8)
    edges = [
        (0, 1), (0, 2), (0, 3),
        (1, 2), (1, 3),
        (2, 3),
        (3, 5),
        (4, 5), (4, 6), (4, 7),
        (5, 6),
        (6, 7)
    ]
    
    for s, d in edges:
        g.add_edge(s, d)
    
    return g

if __name__ == "__main__":
    g = create_graph()
    g.print_graph()
