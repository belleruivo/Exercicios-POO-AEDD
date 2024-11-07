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

from stack import Stack

def mostrar_pares_cadastrados(stack):
    elementos = stack.get_all_elements()

    if len(elementos) < 2:
        print("Não há elementos suficientes na pilha para formar um intervalo.")
        return []

    primeiro = elementos[0]  
    ultimo = elementos[-1]   

    intervalo_pares = [num for num in elementos[1:-1] if num % 2 == 0]

    print(f"Números pares entre o primeiro ({primeiro}) e o último ({ultimo}) elemento da lista: {intervalo_pares}")
    return intervalo_pares

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
                mostrar_pares_cadastrados(pilha)

        elif opcao == '3':
            if pilha.is_empty():
                print("A pilha está vazia. Não há números para excluir.")
            else:
                elementos = pilha.get_all_elements()
                print("Números cadastrados na pilha: ", elementos)
                numero_escolhido = int(input("Digite o número que deseja excluir: "))

                numero_excluido = pilha.remove(numero_escolhido)
                if numero_excluido is not None:
                    print(f"Número {numero_excluido} excluído da pilha.")
                else:
                    print(f"O número {numero_escolhido} não foi encontrado na pilha.")

        elif opcao == '4':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

main()