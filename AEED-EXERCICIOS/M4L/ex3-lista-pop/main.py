from node import Node  # importando a classe Node
from pop_function import pop  # importando a função pop

# função para criar uma lista ligada a partir de uma lista de valores
def criar_lista_ligada(valores):
    if not valores:  # verifica se a lista de valores está vazia
        return None  # retorna None se não houver valores
    head = Node(valores[0])  # cria o nó cabeça com o primeiro valor
    current = head  # variável para percorrer a lista
    for valor in valores[1:]:  # percorre os valores restantes
        current.next = Node(valor)  # cria um novo nó e o conecta ao próximo
        current = current.next  # move para o próximo nó
    return head  # retorna o nó cabeça da lista ligada

# função para imprimir a lista ligada
def imprimir_lista(head):
    current = head  # começa no nó cabeça
    while current:  # enquanto houver um nó
        print(current.data, end=" -> ")  # imprime o dado do nó
        current = current.next  # vai para o próximo nó
    print("None")  # final da lista ligada

# função principal que interage com o usuário
def main():
    try:
        # pede ao usuário para digitar valores inteiros separados por espaço
        valores = list(map(int, input("Digite os valores para a lista ligada separados por espaço: ").split()))
        head = criar_lista_ligada(valores)  # cria a lista ligada com os valores fornecidos
        print("\nLista ligada antes da remoção:")
        imprimir_lista(head)  # imprime a lista ligada antes da remoção

        # pede ao usuário para digitar a posição do item que deseja remover
        position = int(input("\nDigite a posição que deseja remover (começa de 0): "))
        head, item = pop(position, head)  # remove o item na posição especificada
        print(f"\nItem removido: {item}")  # exibe o item removido

        print("\nLista ligada após a remoção:")
        imprimir_lista(head)  # imprime a lista ligada após a remoção
    except ValueError:
        # trata erros de entrada inválida, como valores que não são inteiros
        print("Entrada inválida! Certifique-se de digitar números inteiros.")
    except IndexError as e:
        # trata erros de índice fora dos limites
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()  # executa a função principal
