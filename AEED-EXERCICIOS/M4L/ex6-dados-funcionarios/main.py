# Faça um programa que cadastre n funcionários. Para cada funcionário devem ser
# cadastrados nome e salário. Os dados devem ser armazenados em uma lista
# simplesmente encadeada e ordenada, de forma decrescente, pelo salário do
# funcionário. Posteriormente, o programa de mostrar:
# a. O nome do funcionário que tem o maior salário (em caso de empate mostrar
# todos);
# b. A média salarial de todos os funcionários juntos;
# c. A quantidade de funcionários com salário superior a um valor fornecido pelo
# usuário. Caso nenhum funcionário satisfaça essa condição, mostrar
# mensagem.

from funcionario import Funcionario

def inserir_funcionario(nome, salario, head):
    novo_funcionario = Funcionario(nome, salario)

    # Caso a lista esteja vazia ou o novo salário seja maior que o do primeiro funcionário
    if head is None or salario > head.salario:
        novo_funcionario.next = head
        return novo_funcionario  # O novo funcionário é o novo "head" da lista

    # Caso contrário, percorre a lista para encontrar a posição correta
    current = head
    while current.next is not None and current.next.salario >= salario:
        current = current.next

    # Insere o novo funcionário na posição correta
    novo_funcionario.next = current.next
    current.next = novo_funcionario
    return head

def maior_salario(head):
    if not head:
        return None
    
    max_salario = head.salario
    funcionarios = []
    
    current = head
    while current:
        if current.salario == max_salario:
            funcionarios.append(current.nome)
        elif current.salario > max_salario:
            max_salario = current.salario
            funcionarios = [current.nome]
        current = current.next

    return funcionarios

def calcular_media_salarial(head):
    if not head:
        return 0.0
    
    total_salario = 0
    total_funcionarios = 0
    
    current = head
    while current:
        total_salario += current.salario
        total_funcionarios += 1
        current = current.next

    return total_salario / total_funcionarios if total_funcionarios > 0 else 0.0

def contar_funcionarios_acima_salario(head, valor):
    count = 0
    current = head
    while current:
        if current.salario > valor:
            count += 1
        current = current.next
    return count

def imprimir_lista(head):
    current = head
    while current:
        print(f'Nome: {current.nome}, Salário: {current.salario}')
        current = current.next

def main():
    head = None
    n = int(input("Digite o número de funcionários a serem cadastrados: "))

    for _ in range(n):
        nome = input("Digite o nome do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        head = inserir_funcionario(nome, salario, head)
    
    print("\nFuncionários cadastrados (em ordem decrescente de salário):")
    imprimir_lista(head)

    funcionarios_maior_salario = maior_salario(head)
    print("\nFuncionário(s) com o maior salário:")
    for nome in funcionarios_maior_salario:
        print(nome)

    media = calcular_media_salarial(head)
    print(f"\nMédia salarial dos funcionários: R$ {media:.2f}")
    
    valor = float(input("\nDigite o valor para verificar a quantidade de funcionários com salário superior a: R$ "))
    count = contar_funcionarios_acima_salario(head, valor)
    if count > 0:
        print(f"Quantidade de funcionários com salário superior a R$ {valor:.2f}: {count}")
    else:
        print(f"Nenhum funcionário tem salário superior a R$ {valor:.2f}.")

main()
