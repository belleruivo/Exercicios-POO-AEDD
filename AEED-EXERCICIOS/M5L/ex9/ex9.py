'''9. Faça um programa que apresente o menu de opções abaixo:
MENU
1- Cadastrar número
2- Mostrar números pares entre o primeiro e o último número cadastrado
3- Excluir número
4- Sair
Observações:
a. O programa deve ser implementado usando uma estrutura do tipo pilha.
b. A opção 1 do menu cadastra um número de cada vez.
c. Mostrar mensagem para opção inválida do menu.
d. Cuidado com o intervalo de números formado pelo primeiro e pelo último
    número da pilha, pois este pode ser crescente, decrescente ou ainda ser o
    mesmo número.
e. Quando a opção do menu não puder ser realizada, mostrar mensagem.'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("A pilha está vazia. Não há números para excluir.")
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def get_all_elements(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements

def mostrar_pares(inicio, fim):
    if inicio > fim:
        inicio, fim = fim, inicio  # Inverte se necessário

    pares = [num for num in range(inicio, fim + 1) if num % 2 == 0]
    return pares

def main():
    pilha = Stack()

    while True:
        print("\nMENU")
        print("1 - Cadastrar número")
        print("2 - Mostrar números pares entre o primeiro e o último número cadastrado")
        print("3 - Excluir número")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            numero = int(input("Digite um número para cadastrar: "))
            pilha.push(numero)
            print(f"Número {numero} cadastrado com sucesso.")

        elif opcao == '2':
            if pilha.is_empty():
                print("A pilha está vazia. Nenhum número cadastrado.")
            else:
                elementos = pilha.get_all_elements()
                primeiro = elementos[-1]  # O primeiro número cadastrado
                ultimo = elementos[0]      # O último número cadastrado
                pares = mostrar_pares(primeiro, ultimo)
                print(f"Números pares entre {primeiro} e {ultimo}: {pares}")

        elif opcao == '3':
            numero_excluido = pilha.pop()
            if numero_excluido is not None:
                print(f"Número {numero_excluido} excluído da pilha.")

        elif opcao == '4':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
