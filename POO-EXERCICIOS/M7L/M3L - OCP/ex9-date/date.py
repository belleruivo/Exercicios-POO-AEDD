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


