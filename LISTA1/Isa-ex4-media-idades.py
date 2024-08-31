'''
4. Desejando obter a média aritmética das idades dos alunos do curso de Odontologia,
do primeiro ano, do ano de 2023, construir um programa que leia, calcule e mostre a
média aritmética das idades. O programa é encerrado quando for lida uma idade igual
a zero e deve rejeitar idades negativas, pedindo que o usuário redigite. 
'''

print("------------------------------------------------------------------------------------------------")
print("Olá, seja bem-vindo(a) ao programa que calcula a média aritmética das idades dos alunos de Odonto do ano de 2023!")
print("------------------------------------------------------------------------------------------------")

while True:
    try:
        idade = int(input("Digite a idade do aluno (ou 0 (zero) para encerrar): "))

        if idade == 0:
            break
        elif: idade < 0:
            print("Idade inválida. Por favor, digite um número inteiro positivo.")
            continue
        else:
            total_idades += idade
            quantidade_alunos += 1
    except