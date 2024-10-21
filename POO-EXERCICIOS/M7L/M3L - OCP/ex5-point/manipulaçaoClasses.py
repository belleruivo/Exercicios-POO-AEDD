import math

class MovimentoDePonto:
    @staticmethod
    def mover(ponto, dx, dy):
        ponto.set_x(ponto.get_x() + dx)
        ponto.set_y(ponto.get_y() + dy)

class DistanciaPontos:
    @staticmethod
    def calcular(ponto1, ponto2):
        dx = ponto2.get_x() - ponto1.get_x()
        dy = ponto2.get_y() - ponto1.get_y()
        return math.sqrt(dx**2 + dy**2)
    
class RotacaoPontos:
    @staticmethod #aqui foi adicionado mais uma classe para mostrar como não interfere na classe principal Point
    def rotacionar(ponto, angulo, origem_x=0, origem_y=0):
        rad = math.radians(angulo)
        x_rotacionado = origem_x + math.cos(rad) * (ponto.get_x() - origem_x) - math.sin(rad) * (ponto.get_y() - origem_y)
        y_rotacionado = origem_y + math.sin(rad) * (ponto.get_x() - origem_x) + math.cos(rad) * (ponto.get_y() - origem_y)
        ponto.set_x(x_rotacionado)
        ponto.set_y(y_rotacionado)