'''
Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.
'''

from datetime import datetime
import calendar
import locale

# Configura a localidade para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

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
        

class FormatadorData:
    def __init__(self, data):
        self.data = data
    
    def formatar_data(self, formato="padrao"):
        if formato == "iso":
            return f"{self.data.ano}-{self.data.mes:02}-{self.data.dia:02}"
        elif formato == "us":
            return f"{self.data.mes:02}/{self.data.dia:02}/{self.data.ano}"
        else:
            return f"{self.data.dia:02}/{self.data.mes:02}/{self.data.ano}"

def obter_dia(mes, ano):
    while True:
        try:
            dia = int(input("Digite o dia: "))
            dias_no_mes = calendar.monthrange(ano, mes)[1]  # Quantidade de dias no mês e ano especificados
            if 1 <= dia <= dias_no_mes:
                return dia
            else:
                # Obtém o nome do mês em português
                nome_mes = datetime(ano, mes, 1).strftime('%B').capitalize()
                print(f"Dia inválido! {nome_mes} de {ano} tem apenas {dias_no_mes} dias.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_mes():
    while True:
        try:
            mes = int(input("Digite o mês: "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Mês inválido. Insira um valor entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_ano():
    while True:
        ano = input("Digite o ano (4 dígitos): ").strip()
        if len(ano) == 4 and ano.isdigit():
            return int(ano)  
        else:
            print("Entrada inválida. O ano deve ter exatamente 4 dígitos.\n")

def main():
    print("-=" * 30)
    while True:
        try:
            ano = obter_ano()
            mes = obter_mes()
            dia = obter_dia(mes, ano)
            
            data = datetime(ano, mes, dia)
            data_obj = Date(dia, mes, ano)
            
            # Usa o FormatadorData para formatos personalizados
            formatador = FormatadorData(data_obj)
            print("\nFormato ISO:", formatador.formatar_data("iso"))
            print("Formato US:", formatador.formatar_data("us"))
            print("Formato Padrão:", formatador.formatar_data())
            break  
        except ValueError:
            print("Ops! Algo deu errado com a sua data. Por favor, insira uma data válida.\n")

    print("-=" * 30)

main()