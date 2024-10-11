from point import Point
from manipulaçaoClasses import *

#função auxiliar ou utilitária que não depende diretamente dos 
#atributos ou comportamento de uma instância de objeto

def obter_coordenada(mensagem):                                  
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um caractere numérico.\n")

def main():
    print("-=" * 30)
    print("Insira as coordenadas do primeiro ponto:")
    x1 = obter_coordenada("Digite o valor de x1: ")
    y1 = obter_coordenada("Digite o valor de y1: ")
    ponto1 = Point(x1, y1)

    print("\nInsira as coordenadas do segundo ponto:")
    x2 = obter_coordenada("Digite o valor de x2: ")
    y2 = obter_coordenada("Digite o valor de y2: ")
    ponto2 = Point(x2, y2)

    print("\nPonto 1:")
    ponto1.exibir()

    print("\nPonto 2:")
    ponto2.exibir()

    print("\nAgora, vamos mover o primeiro ponto.")
    dx = obter_coordenada("Digite o deslocamento em x (dx): ")
    dy = obter_coordenada("Digite o deslocamento em y (dy): ")
    MovimentoDePonto.mover(ponto1, dx, dy)

    print("\nPonto 1 após o movimento:")
    ponto1.exibir()

    distancia = DistanciaPontos.calcular(ponto1, ponto2)
    print(f"\nA distância entre o ponto 1 e o ponto 2 é: {distancia:.2f}")

    angulo = obter_coordenada("Digite o ângulo de rotação em graus: ")
    RotacaoPontos.rotacionar(ponto1, angulo)

    print("\nPonto 1 após a rotação:")
    ponto1.exibir()

    print("-=" * 30)

main()


