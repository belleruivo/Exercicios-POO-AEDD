from date import Date
from formatar import *
from entradas import *

def main():
    print("-=" * 30)
    while True:
        try:
            ano = obter_ano()
            mes = obter_mes()
            dia = obter_dia(mes, ano)
            
            data_obj = Date(dia, mes, ano)
            
            # Usa diferentes formatadores
            print("\nFormato ISO:", data_obj.formatar_data(FormatadorISO()))
            print("Formato US:", data_obj.formatar_data(FormatadorUS()))
            print("Formato Padrão:", data_obj.formatar_data(FormatadorPadrao()))
            break  
        except ValueError:
            print("Ops! Algo deu errado com a sua data. Por favor, insira uma data válida.\n")

    print("-=" * 30)

main()