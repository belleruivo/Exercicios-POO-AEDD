# Faça um programa que cadastre n alunos. Para cada aluno devem ser cadastrados:
# nome, nota1 e nota2. Primeiro, liste todos os alunos cadastrados, ordenando-os pela
# média ponderada das notas, tendo a primeira nota peso 2 e a segunda, peso 3. Em
# seguida, ordene os alunos, de forma crescente, pela nota1, e liste-os. Finalmente,
# considerando que, para ser aprovado, o aluno deve ter no mínimo média 7, liste, em
# ordem alfabética, os alunos reprovados. Em cada ordenação use um algoritmo
# diferente.

print("-"*30)
print("      CADASTRO DE ALUNOS")
print("-"*30)
def bubble_sort_por_media(alunos):
    n = len(alunos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if alunos[j]['media'] > alunos[j + 1]['media']:
                alunos[j], alunos[j + 1] = alunos[j + 1], alunos[j]  # Troca

def insertion_sort_por_nota1(alunos):
    for i in range(1, len(alunos)):
        chave = alunos[i]
        j = i - 1
        while j >= 0 and alunos[j]['nota1'] > chave['nota1']:
            alunos[j + 1] = alunos[j]
            j -= 1
        alunos[j + 1] = chave

def selection_sort_reprovados(reprovados):
    n = len(reprovados)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if reprovados[j]['nome'] < reprovados[menor]['nome']:
                menor = j
        reprovados[i], reprovados[menor] = reprovados[menor], reprovados[i]  # Troca

def main():
    numAlunos = int(input("Digite quantos alunos deseja cadastrar: "))
    alunos = []

    for _ in range(numAlunos):
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        
        media = (nota1 * 2 + nota2 * 3) / (2 + 3)  # Cálculo da média ponderada
        
        alunos.append({'nome': nome, 'nota1': nota1, 'nota2': nota2, 'media': media})

    # Ordenação por média ponderada usando Bubble Sort
    bubble_sort_por_media(alunos)
    print("\nAlunos ordenados por média ponderada:")
    for aluno in alunos:
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")

    # Ordenação por nota1 usando Insertion Sort
    insertion_sort_por_nota1(alunos)
    print("\nAlunos ordenados por nota1:")
    for aluno in alunos:
        print(f"{aluno['nome']} - Nota1: {aluno['nota1']}")

    reprovados = [aluno for aluno in alunos if aluno['media'] < 7]
    selection_sort_reprovados(reprovados)
    
    print("\nAlunos reprovados em ordem alfabética:")
    for aluno in reprovados:
        print(aluno['nome'])

main()


    