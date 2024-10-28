# Crie uma classe chamada Calendar que represente um calendário anual. Essa classe
# deve ter métodos para exibir o calendário de um determinado mês, verificar se uma
# data é feriado e calcular a diferença de dias entre duas datas.

import calendar
from datetime import datetime, timedelta


class Calendar:
    def __init__(self, ano):
        self.ano = ano
        self.feriados = self.definir_feriados()
    
    def definir_feriados(self):
        return {
            "01/01": "Ano Novo",
            "25/12": "Natal",
            "07/09": "Independência do Brasil",
            "15/11": "Proclamação da República",
            "01/05": "Dia do Trabalho",
        }

    def exibir_calendario_mes(self, mes):
        print(calendar.month(self.ano, mes))

    def verificar_feriado(self, data_str):
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            data_formatada = data.strftime("%d/%m")
            if data_formatada in self.feriados:
                return f"{data_str} é feriado: {self.feriados[data_formatada]}"
            else:
                return f"{data_str} não é feriado."
        except ValueError:
            return "Data inválida. Por favor, use o formato DD/MM/AAAA."

    def calcular_diferenca_dias(self, data1_str, data2_str):
        try:
            data1 = datetime.strptime(data1_str, "%d/%m/%Y")
            data2 = datetime.strptime(data2_str, "%d/%m/%Y")
            diferenca = abs((data2 - data1).days)
            return f"A diferença entre {data1_str} e {data2_str} é de {diferenca} dias."
        except ValueError:
            return "Uma ou ambas as datas são inválidas. Por favor, use o formato DD/MM/AAAA."

calendario = Calendar(2024)

calendario.exibir_calendario_mes(1)

print(calendario.verificar_feriado("01/01/2024"))  
print(calendario.verificar_feriado("25/12/2024"))  
print(calendario.verificar_feriado("05/02/2024"))  

#  diferença de dias entre duas datas
print(calendario.calcular_diferenca_dias("01/01/2024", "25/12/2024"))  
print(calendario.calcular_diferenca_dias("01/01/2024", "01/01/2024")) 
