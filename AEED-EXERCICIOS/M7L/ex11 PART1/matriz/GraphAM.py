class GraphAM:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, src, dest):
        self.graph[src][dest] = 1
        self.graph[dest][src] = 1

    def print_graph(self):
        for row in self.graph:
            print(", ".join(map(str, row)))
