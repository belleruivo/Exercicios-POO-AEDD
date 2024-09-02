'''
4. Desejando obter a média aritmética das idades dos alunos do curso de Odontologia,
do primeiro ano, do ano de 2023, construir um programa que leia, calcule e mostre a
média aritmética das idades. O programa é encerrado quando for lida uma idade igual
a zero e deve rejeitar idades negativas, pedindo que o usuário redigite. 
'''

print("------------------------------------------------------------------------------------------------")
print("Olá, seja bem-vindo(a) ao programa que calcula a média aritmética das idades dos alunos de Odonto do ano de 2023!")
print("------------------------------------------------------------------------------------------------")

total_idades = 0
quantidade_alunos = 0
idades_digitadas = []  # Lista para armazenar as idades digitadas

while True:
    try:
        idade = int(input("Digite a idade do aluno (ou 0 (zero) para encerrar): "))

        if idade == 0:
            break
        elif idade < 0 or idade > 100:
            print("Idade inválida. Por favor, digite um número inteiro positivo e menor ou igual a 100.")
            continue
        else:
            total_idades += idade
            quantidade_alunos += 1
            idades_digitadas.append(idade)  # Adiciona a idade à lista de idades digitadas
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")
        
if quantidade_alunos > 0:
    media_idade = total_idades / quantidade_alunos
    print(f"\nAs idades digitadas foram: {idades_digitadas}")
    print(f"\nA soma das idades: {total_idades}")
    print(f"\nQuantidade de idades digitadas no total: {quantidade_alunos}")
    print(f"\nA média aritmética das idades dos alunos é: {total_idades} \ {quantidade_alunos} = {media_idade:.2f} anos.")
else:
    print("\nNenhuma idade válida foi inserida.")
