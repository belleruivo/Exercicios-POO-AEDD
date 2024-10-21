import calendar
import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def obter_dia(mes, ano):
    while True:
        try:
            dia = int(input("Digite o dia: "))
            dias_no_mes = calendar.monthrange(ano, mes)[1]
            if 1 <= dia <= dias_no_mes:
                return dia
            else:
                nome_mes = datetime(ano, mes, 1).strftime('%B').capitalize()
                print(f"Dia inválido! {nome_mes} de {ano} tem apenas {dias_no_mes} dias.\n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.\n")

def obter_mes():
    while True:
        try:
            mes = int(input("Digite o mês: "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Mês inválido. Insira um valor entre 1 e 12.\n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.\n")

def obter_ano():
    while True:
        ano = input("Digite o ano (4 dígitos): ").strip()
        if len(ano) == 4 and ano.isdigit():
            return int(ano)  
        else:
            print("Entrada inválida. O ano deve ter exatamente 4 dígitos.\n")
