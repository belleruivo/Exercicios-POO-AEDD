'''
4. Desejando obter a média aritmética das idades dos alunos do curso de Odontologia,
do primeiro ano, do ano de 2023, construir um programa que leia, calcule e mostre a
média aritmética das idades. O programa é encerrado quando for lida uma idade igual
a zero e deve rejeitar idades negativas, pedindo que o usuário redigite. 
'''
print("------------------------------------------------------------------------------------------------")
print("Olá, seja bem-vindo(a) ao programa que calcula a média aritmética das idades dos alunos de Odonto do ano de 2023!")
print("------------------------------------------------------------------------------------------------")

def ler_idade():
    while True:
        try:
            idade = int(input("Digite a idade do aluno (ou 0 (zero) para encerrar): "))
            if idade == 0:
                return 0
            elif idade < 0 or idade > 100:
                print("Idade inválida. Por favor, digite um número inteiro positivo e menor ou igual a 100.")
            else:
                return idade
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

def calcular_media(total_idades, quantidade_alunos):
    if quantidade_alunos > 0:
        return total_idades / quantidade_alunos
    else:
        return 0

def main():

    total_idades = 0
    quantidade_alunos = 0
    idades_digitadas = []

    while True:
        idade = ler_idade()
        if idade == 0:
            break
        total_idades += idade
        quantidade_alunos += 1
        idades_digitadas.append(idade)

    media_idade = calcular_media(total_idades, quantidade_alunos)

    if quantidade_alunos > 0:
        print(f"\nAs idades digitadas foram: {idades_digitadas}")
        print(f"A soma das idades: {total_idades}")
        print(f"Quantidade de idades digitadas no total: {quantidade_alunos}")
        print(f"A média aritmética das idades dos alunos é: {total_idades} / {quantidade_alunos} = {media_idade:.2f} anos.\n")
    else:
        print("\nNenhuma idade válida foi inserida.")

if __name__ == "__main__":
    main()