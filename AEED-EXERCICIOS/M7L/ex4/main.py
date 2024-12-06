'''4. Implemente um algoritmo para verificar se um grafo e acíclico utilizando o algoritmo
de busca em profundidade.'''

# M7L/ex4/main.py
class Graph:
    '''Classe que representa um grafo e contém métodos para verificar se é acíclico.'''

    def __init__(self):
        '''Inicializa um grafo vazio.'''
        self.graph = {}

    def add_edge(self, u, v):
        '''Adiciona uma aresta ao grafo.'''
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def is_acyclic(self):
        '''Verifica se o grafo é acíclico utilizando busca em profundidade (DFS).'''
        visited = set()  # Conjunto para rastrear os nós visitados
        rec_stack = set()  # Conjunto para rastrear os nós na pilha de recursão

        def dfs(v):
            '''Função auxiliar para realizar a busca em profundidade.'''
            visited.add(v)  # Marca o nó atual como visitado
            rec_stack.add(v)  # Adiciona o nó atual à pilha de recursão

            for neighbor in self.graph.get(v, []):  # Itera sobre os vizinhos do nó atual
                if neighbor not in visited:  # Se o vizinho não foi visitado
                    if dfs(neighbor):  # Chama recursivamente a função DFS
                        return True  # Se um ciclo for encontrado, retorna True
                elif neighbor in rec_stack:  # Se o vizinho está na pilha de recursão
                    return True  # Um ciclo foi encontrado

            rec_stack.remove(v)  # Remove o nó da pilha de recursão ao final da exploração
            return False  # Retorna False se não houver ciclo

        for node in self.graph:  # Itera sobre todos os nós do grafo
            if node not in visited:  # Se o nó não foi visitado
                if dfs(node):  # Chama a função DFS
                    return False  # Se um ciclo for encontrado, retorna False
        return True  # Retorna True se o grafo for acíclico

# Exemplo de uso
g = Graph()  # Cria uma instância do grafo
g.add_edge(0, 1)  # Adiciona arestas
g.add_edge(1, 2)
g.add_edge(2, 0)  # Grafo cíclico
print(g.is_acyclic())  # Saída: False
g = Graph()  # Cria uma nova instância do grafo
g.add_edge(0, 1)  # Adiciona arestas
g.add_edge(1, 2)
print(g.is_acyclic())  # Saída: True