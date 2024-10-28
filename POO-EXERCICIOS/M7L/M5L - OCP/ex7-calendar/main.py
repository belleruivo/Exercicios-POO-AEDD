
from my_calendar import Calendar

def main():

    calendario = Calendar(2024)

    calendario.exibir_calendario_mes(1)

    print(calendario.verificar_feriado("01/01/2024"))  
    print(calendario.verificar_feriado("25/12/2024"))  
    print(calendario.verificar_feriado("05/02/2024"))  

    #  diferença de dias entre duas datas
    print(calendario.calcular_diferenca_dias("01/01/2024", "25/12/2024"))  
    print(calendario.calcular_diferenca_dias("01/01/2024", "01/01/2024")) 