import math

class Ponto:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def exibir(self):
        print(f"Ponto(x: {self.x}, y: {self.y})")

class ManipuladorDePonto:
    @staticmethod
    def mover(ponto, dx, dy):
        ponto.set_x(ponto.get_x() + dx)
        ponto.set_y(ponto.get_y() + dy)

    @staticmethod
    def calcular_distancia(ponto1, ponto2):
        dx = ponto2.get_x() - ponto1.get_x()
        dy = ponto2.get_y() - ponto1.get_y()
        return math.sqrt(dx**2 + dy**2)

    @staticmethod
    def rotacionar(ponto, angulo, origem_x=0, origem_y=0):
        """Rotaciona o ponto em relação à origem especificada por um ângulo em graus."""
        rad = math.radians(angulo)
        x_rotacionado = origem_x + math.cos(rad) * (ponto.get_x() - origem_x) - math.sin(rad) * (ponto.get_y() - origem_y)
        y_rotacionado = origem_y + math.sin(rad) * (ponto.get_x() - origem_x) + math.cos(rad) * (ponto.get_y() - origem_y)
        ponto.set_x(x_rotacionado)
        ponto.set_y(y_rotacionado)

def obter_coordenada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um caractere numérico.\n")

def main():
    print("-=" * 30)
    print("Insira as coordenadas do ponto:")
    x = obter_coordenada("Digite o valor de x: ")
    y = obter_coordenada("Digite o valor de y: ")
    ponto = Ponto(x, y)

    print("\nPonto original:")
    ponto.exibir()

    # Movendo o ponto
    dx = obter_coordenada("Digite o deslocamento em x (dx): ")
    dy = obter_coordenada("Digite o deslocamento em y (dy): ")
    ManipuladorDePonto.mover(ponto, dx, dy)
    print("\nPonto após o movimento:")
    ponto.exibir()

    # Rotacionando o ponto
    angulo = obter_coordenada("Digite o ângulo de rotação em graus: ")
    ManipuladorDePonto.rotacionar(ponto, angulo)
    print("\nPonto após a rotação:")
    ponto.exibir()

    print("-=" * 30)

main()