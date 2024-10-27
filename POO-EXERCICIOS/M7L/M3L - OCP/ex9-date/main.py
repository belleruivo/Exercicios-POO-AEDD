'''
Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.
'''

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

            print("\nFormato ISO:", data_obj.formatar_data(FormatadorISO()))
            print("Formato US:", data_obj.formatar_data(FormatadorUS()))
            print("Formato Padrão:", data_obj.formatar_data(FormatadorPadrao()))
            break  
        except ValueError:
            print("Ops! Algo deu errado com a sua data. Por favor, insira uma data válida.\n")

    print("-=" * 30)

main()