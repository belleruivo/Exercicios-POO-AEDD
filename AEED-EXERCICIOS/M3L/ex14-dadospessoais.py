'''
Elabore um programa que armazene os seguintes dados de n pessoas: nome, idade e sexo. O programa deve apresentar os dados em:
a. Ordem crescente alfabética de nome (use o quickSort).
b. Ordem decrescente de idade (use o bubbleSort).
'''

def quickSort(lst, key):
    """Ordena a lista usando o algoritmo QuickSort, baseado na chave de ordenação (key)."""
    if len(lst) <= 1:  # Caso base: se a lista tem 1 ou nenhum elemento, já está ordenada.
        return lst
    pivot = lst[0][key]  # Pivô é o primeiro elemento, baseado na chave 'key' (nome)
    less = [x for x in lst[1:] if x[key] <= pivot]  # Sublista com elementos menores ou iguais ao pivô
    greater = [x for x in lst[1:] if x[key] > pivot]  # Sublista com elementos maiores que o pivô
    return quickSort(less, key) + [lst[0]] + quickSort(greater, key)  # Recursão nas sublistas

def bubbleSort(lst, key):
    """Ordena a lista usando o algoritmo Bubble Sort com melhoria (tweak), com base na chave de ordenação (key)."""
    n = len(lst)  # Tamanho da lista
    while n > 1:  # Enquanto ainda houver elementos a ordenar
        swapped = False  # Flag para verificar se houve troca
        i = 1  # Começa a comparar do segundo elemento
        while i < n:
            if lst[i][key] > lst[i-1][key]:  # Compara as idades, se a idade de i for maior que i-1, troca
                lst[i], lst[i-1] = lst[i-1], lst[i]  # Troca os elementos de lugar
                swapped = True  # Marca que houve troca
            i += 1
        if not swapped:  # Se não houve troca, a lista já está ordenada
            return
        n -= 1  # Reduz a comparação para a parte não ordenada da lista

def main():
    n = int(input("Quantas pessoas você deseja cadastrar? "))
    
    pessoas = []
    for i in range(n):
        nome = input(f"Digite o nome da {i+1}ª pessoa: ")
        idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
        sexo = input(f"Digite o sexo da {i+1}ª pessoa (M/F): ")
        pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})
    
    pessoas_ordenadas_nome = quickSort(pessoas, "nome")
    print("\nPessoas ordenadas por nome (alfabeticamente):")
    for pessoa in pessoas_ordenadas_nome:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}")
    
    bubbleSort(pessoas, "idade")
    print("\nPessoas ordenadas por idade (decrescente):")
    for pessoa in pessoas:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}")

if __name__ == "__main__":
    main()
