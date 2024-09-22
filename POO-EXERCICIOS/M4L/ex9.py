'''
Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.
'''

from datetime import datetime
class Date:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    def getDia(self):
        return self.dia
    
    def getMes(self):
        return self.mes
    
    def getAno(self):
        return self.ano
    
    def setDia(self, dia):
        self.dia = dia
        
    def setMes(self, mes):
        self.mes = mes
        
    def setAno(self, ano):
        self.ano = ano
        
    def imprimir_data(self):
        print(f"\nData: {self.dia:02}/{self.mes:02}/{self.ano}")

def main():
    print("-=" * 30)

    while True:
        try:
            while True:
                try:
                    dia = int(input("Digite o dia: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número inteiro.\n")

            while True:
                try:
                    mes = int(input("Digite o mês: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número inteiro.\n")

            while True:
                ano = input("Digite o ano (4 dígitos): ").strip()
                if len(ano) == 4 and ano.isdigit():
                    ano = int(ano)
                    break
                else:
                    print("Entrada inválida. O ano deve ter exatamente 4 dígitos.\n")

            data = datetime(ano, mes, dia)
            data_obj = Date(dia, mes, ano)
            data_obj.imprimir_data()
            break  
        except ValueError:
            print("Ops! Algo deu errado com a sua data. Por favor, insira uma data válida.\n")

    print("-=" * 30)

main()