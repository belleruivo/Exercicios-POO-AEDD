'''1. Escreva um programa que, dados uma matriz de adjacência e dois nós de um grafo,
calcule:
a. O número de caminhos de determinado comprimento existentes entre eles.
b. O número total de caminhos existentes entre eles.'''

import numpy as np

def count_paths(adjacency_matrix, start_node, end_node, path_length=None):
    """
    Calcula o número de caminhos entre dois nós em um grafo.
    """
    # Transforma a matriz de adjacência em numpy array, se não for
    adjacency_matrix = np.array(adjacency_matrix)
    
    # Número de nós no grafo
    n = len(adjacency_matrix)
    
    if path_length is not None:
        # Eleva a matriz de adjacência à potência do comprimento do caminho
        power_matrix = np.linalg.matrix_power(adjacency_matrix, path_length)
        # Retorna o número de caminhos de comprimento específico
        return power_matrix[start_node, end_node]
    else:
        # Soma todas as potências da matriz de adjacência até n-1
        total_paths_matrix = np.zeros((n, n), dtype=int)
        for k in range(1, n):  # Caminhos de comprimento 1 até n-1
            total_paths_matrix += np.linalg.matrix_power(adjacency_matrix, k)
        # Retorna o número total de caminhos
        return total_paths_matrix[start_node, end_node]

# Exemplo de uso
if __name__ == "__main__":
    # Matriz de adjacência do grafo
    adjacency_matrix = [
    [0, 1],
    [1, 0],
    ]
    
    start_node = 0  # Nó inicial
    end_node = 1    # Nó final
    
    # Número de caminhos de comprimento específico (exemplo: 2)
    path_length = 2
    specific_paths = count_paths(adjacency_matrix, start_node, end_node, path_length)
    print(f"Number of paths of length {path_length} from node {start_node} to node {end_node}: {specific_paths}")
    
    # Número total de caminhos entre os nós
    total_paths = count_paths(adjacency_matrix, start_node, end_node)
    print(f"Total number of paths from node {start_node} to node {end_node}: {total_paths}")
