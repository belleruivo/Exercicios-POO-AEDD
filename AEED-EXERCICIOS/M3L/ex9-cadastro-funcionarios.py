'''9. Faça um programa que cadastre o nome e o salário de n funcionários. Usando um
método de ordenação diferente para cada item a seguir, liste todos os dados dos
funcionários das seguintes formas:
a. Em ordem crescente de salário;
b. Em ordem decrescente de salário;
c. Em ordem alfabética.'''

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def selectionSort(list):
    for i in range(len(list)):
        maxIndex = i
        for j in range(i+1, len(list)):
            if list[j] > list[maxIndex]:
                maxIndex = j
        if maxIndex !=i:
            swap(list, maxIndex, i)

def insertionSort(list):
    for i in range(1, len(list)):
        itemToInsert = list[i]
        j = i -1
        while j >= 0 and itemToInsert < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = itemToInsert

def bubbleSort(list):
    n = len(list)
    while n  > 1:
        swapped = False
        i = 1
        while i < n:
            if list[i] < list[i-1]:
                swap(list, i, i-1)
                swapped = True
            i += 1
        if not swapped:return
        n -=1

def cadastrar_funcionarios():
    funcionarios = []
    
    while True:
        try:
            n = int(input("Quantos funcionários deseja cadastrar? "))
            if n <= 0:
                print("O número de funcionários deve ser maior que zero.\n")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido.\n")

    for i in range(n):
        while True:
            nome = input(f"\nDigite o nome do funcionário {i + 1}: ")
            if not nome:
                print("O nome não pode estar vazio.")
            else:
                break 
        
        while True:
            try:
                salario = float(input(f"Digite o salário do funcionário {i + 1}: "))
                if salario < 0:
                    print("O salário não pode ser negativo.")
                    continue
                break 
            except ValueError:
                print("Por favor, insira um valor de salário válido.\n")
    
        funcionarios.append([nome, salario])

    return funcionarios

def exibir_funcionarios(funcionarios, titulo):
    print(f"\n{titulo}:")
    for nome, salario in funcionarios:
        print(f"Nome: {nome}, Salário: R${salario:.2f}")

def main():
    funcionarios = cadastrar_funcionarios()

    funcionarios_crescente_salario = funcionarios[:]
    insertionSort(funcionarios_crescente_salario)
    exibir_funcionarios(funcionarios_crescente_salario, "Funcionários em ordem crescente de salário")

    funcionarios_decrescente_salario = funcionarios[:]
    selectionSort(funcionarios_decrescente_salario)
    exibir_funcionarios(funcionarios_decrescente_salario, "Funcionários em ordem decrescente de salário")

    funcionarios_alfabetica = funcionarios[:]
    bubbleSort(funcionarios_alfabetica)
    exibir_funcionarios(funcionarios_alfabetica, "Funcionários em ordem alfabética")


main()
