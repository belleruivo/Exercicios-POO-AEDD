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
        
    def get_dia(self):
        return self.dia
    
    def get_mes(self):
        return self.mes
    
    def get_ano(self):
        return self.ano
    
    def set_dia(self, dia):
        self.dia = dia
        
    def set_mes(self, mes):
        self.mes = mes
        
    def set_ano(self, ano):
        self.ano = ano
        
    def formatar_data(self, formatador):
        return formatador.formatar(self)


