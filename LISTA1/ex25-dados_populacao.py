'''
25. Foi realizada uma pesquisa de algumas características físicas da população de uma
certa região, a qual foram coletados os seguintes dados referentes a cada habitante
para serem analisados:
• Sexo.
• Cor dos olhos (azuis, verdes, castanhos).
• Cor dos cabelos (louros, castanhos, pretos).
• Idade.
Faça um programa que determine e escreva:
a. O total de entrevistados
b. O total de homens e o total de mulheres entrevistados
c. A maior e a menor idade do conjunto de habitantes;
d. A média de idade do conjunto de habitantes;
e. A percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35
anos inclusive e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor 0 para a idade.
'''

def coletar_dados():
    habitantes = []
    while True:
        try:
            idade = input("Digite a idade do habitante (ou 0 para finalizar): ").strip()
            if not idade.isdigit() or int(idade) < 0 or int(idade) > 120:
                raise ValueError("Idade inválida. Digite um número inteiro positivo e menor que 120 ou 0 para finalizar.")
            idade = int(idade)
            if idade == 0:
                break

            while True:
                sexo = input("Digite o sexo do habitante (M/F): ").strip().upper()
                if sexo in ['M', 'F']:
                    break
                print("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")

            while True:
                cor_olhos = input("Digite a cor dos olhos do habitante (azuis, verdes, castanhos): ").strip().lower()
                if cor_olhos in ['azuis', 'verdes', 'castanhos']:
                    break
                print("Cor dos olhos inválida. Escolha entre 'azuis', 'verdes' ou 'castanhos'.")

            while True:
                cor_cabelos = input("Digite a cor dos cabelos do habitante (louros, castanhos, pretos): ").strip().lower()
                if cor_cabelos in ['louros', 'castanhos', 'pretos']:
                    break
                print("Cor dos cabelos inválida. Escolha entre 'louros', 'castanhos' ou 'pretos'.")

            habitantes.append({'idade': idade, 'sexo': sexo, 'cor_olhos': cor_olhos, 'cor_cabelos': cor_cabelos})
        except ValueError as e:
            print(e)
    return habitantes

def total_entrevistados(habitantes):
    return len(habitantes)

def total_homens_mulheres(habitantes):
    homens = sum(1 for h in habitantes if h['sexo'] == 'M')
    mulheres = sum(1 for h in habitantes if h['sexo'] == 'F')
    return homens, mulheres

def maior_menor_idade(habitantes):
    idades = [h['idade'] for h in habitantes]
    return max(idades), min(idades)

def media_idade(habitantes):
    idades = [h['idade'] for h in habitantes]
    return sum(idades) / len(idades)

def percentagem_mulheres_criterios(habitantes):
    mulheres_criterios = [h for h in habitantes if h['sexo'] == 'F' and 18 <= h['idade'] <= 35 and h['cor_olhos'] == 'verdes' and h['cor_cabelos'] == 'louros']
    total_mulheres = sum(1 for h in habitantes if h['sexo'] == 'F')
    if total_mulheres == 0:
        return 0
    return (len(mulheres_criterios) / total_mulheres) * 100

def main():
    habitantes = coletar_dados()
    if not habitantes:
        print("Nenhum dado foi coletado.")
        return

    print(f"Total de entrevistados: {total_entrevistados(habitantes)}")
    homens, mulheres = total_homens_mulheres(habitantes)
    print(f"Total de homens: {homens}")
    print(f"Total de mulheres: {mulheres}")
    maior_idade, menor_idade = maior_menor_idade(habitantes)
    print(f"Maior idade: {maior_idade}")
    print(f"Menor idade: {menor_idade}")
    print(f"Média de idade: {media_idade(habitantes):.2f}")
    print(f"Percentagem de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos louros: {percentagem_mulheres_criterios(habitantes):.2f}%")

if __name__ == "__main__":
    main()