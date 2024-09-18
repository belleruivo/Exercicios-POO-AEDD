'''
Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.
'''

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
        return f"{self.dia}/{self.mes}/{self.ano}"
    
def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Insira o mês: "))
    ano = int(input("Digite o ano: "))
        
    data = Date(dia, mes, ano)
        
    data.imprimir_data()
        
main()