'''Faça um programa que cadastre n alunos. Para cada aluno devem ser cadastrados
nome e nota final. Os dados devem ser armazenados em uma lista duplamente
encadeada e não ordenada. Em seguida, o programa deve mostrar apenas o nome
dos alunos aprovados, ou seja, alunos com nota final de no mínimo 7. Se nenhum
aluno estiver aprovado, mostrar mensagem.'''

from doubly_linked_list import DoublyLinkedList
from aluno import Aluno

def main():
    lista_alunos = DoublyLinkedList()
    n = int(input("Quantos alunos deseja cadastrar? "))

    for _ in range(n):
        nome = input("Nome do aluno: ")
        while True:
            try:
                nota_final = float(input("Nota final do aluno (0 a 10): "))
                if 0 <= nota_final <= 10:
                    break
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
        
        aluno = Aluno(nome, nota_final)
        lista_alunos.append(aluno)

    aprovados = lista_alunos.get_aprovados()
    if aprovados:
        print("Alunos aprovados:")
        for nome in aprovados:
            print(nome)
    else:
        print("Nenhum aluno aprovado.")

if __name__ == "__main__":
    main()