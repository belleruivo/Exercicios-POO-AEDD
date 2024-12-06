'''6. Crie um programa para ler um grafo a partir de um arquivo e armazená-lo em uma
estrutura de lista de adjacência. Crie um formato para o seu arquivo de entrada.'''

# PS C:\Users\Usuario\Desktop\Exercicios-POO-AEDD\AEED-EXERCICIOS\M7L\ex6> & C:/Users/Usuario/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Usuario/Desktop/Exercicios-POO-AEDD/AEED-EXERCICIOS/M7L/ex6/main.py
# {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}

class Grafo:
    def __init__(self):
        self.adjacencia = {}  # Inicializa a lista de adjacência

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 not in self.adjacencia:
            self.adjacencia[vertice1] = []  # Inicializa a lista de adjacência para vertice1
        if vertice2 not in self.adjacencia:
            self.adjacencia[vertice2] = []  # Inicializa a lista de adjacência para vertice2
        self.adjacencia[vertice1].append(vertice2)  # Adiciona vertice2 à lista de adjacência de vertice1
        self.adjacencia[vertice2].append(vertice1)  # Adiciona vertice1 à lista de adjacência de vertice2

    def __str__(self):
        return str(self.adjacencia)  # Retorna a representação da lista de adjacência

def ler_grafo(arquivo):
    grafo = Grafo()  # Cria uma nova instância da classe Grafo
    with open(arquivo, 'r') as f:  # Abre o arquivo em modo de leitura
        for linha in f:  # Itera sobre cada linha do arquivo
            vertice1, vertice2 = linha.strip().split()  # Divide a linha em dois vértices
            grafo.adicionar_aresta(vertice1, vertice2)  # Adiciona a aresta ao grafo
    return grafo  # Retorna a instância do grafo preenchida

# Exemplo de uso
if __name__ == "__main__":
    grafo = ler_grafo('./grafo.txt')  # Lê o grafo do arquivo
    print(grafo)  # Exibe a lista de adjacência do grafo