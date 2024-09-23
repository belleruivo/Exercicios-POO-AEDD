'''8. Numa universidade, o sistema de avaliação é o seguinte: para passar direto, o aluno
precisa ter média do período (mp) igual ou superior a 7 pontos. Caso contrário, o
aluno será submetido a exame final, sendo a sua média final (mf) calculada pela
seguinte fórmula: mf = 0.6mp + 0.4ne, onde ne é a nota do exame. Essa média final
deverá então ser igual ou superior a 5 pontos para que o aluno seja aprovado. Por
outro lado, a média do período é calculada através da média das notas dos créditos,
cujo número é diferente para cada disciplina. Faça um programa que leia do usuário o
número de créditos da disciplina, as notas dos créditos, e se necessário calcule a
nota que o aluno precisa tirar no exame final para ser aprovado. Se antes de terminar
todos os créditos o aluno já estiver aprovado, avise isso a ele e encerre a leitura de
notas (utilize aqui um comando break).'''

"""
mp >= 7 passar direto
mf = 0.6mp + 0.4ne
mf>= 5 aprovado
ne -> Nota do exame

"""
def calcular_media_parcial(notas):
    return sum(notas) / len(notas) if notas else 0

def calcular_nota_exame(mp):
    return (0.6 * mp - 5) / -0.4

def ler_creditos():
    while True:
        try:
            creditos = int(input("Qual o número de créditos da disciplina: "))
            if creditos <= 0:
                print("O número de créditos deve ser maior que zero. Tente novamente.\n")
                continue
            return creditos
        except ValueError:
            print("Você inseriu um valor errado. Tente novamente\n")

def ler_notas(creditos):
    notas = []
    for c in range(creditos):
        while True:
            try:
                nota = float(input(f"Nota {c + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Você inseriu um valor inválido. Tente novamente.")
    return notas

def main():
    print("-=" * 18, "Cálculo de Média Final", "-=" * 18)

    creditos = ler_creditos()
    notas = ler_notas(creditos)

    mp = calcular_media_parcial(notas)
    print(f"\nMédia parcial: {mp:.2f}")

    if mp >= 7:
        print("\nParabéns! Você passou direto pela matéria.")
    else:
        ne = calcular_nota_exame(mp)
        print(f"""\nInfelizmente você não passou direto.
Para conseguir passar nessa matéria, você terá que tirar no mínimo {ne:.2f} no exame final.""")

    print("-=" * 48)

main()