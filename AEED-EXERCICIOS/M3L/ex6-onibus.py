'''
Dada uma tabela de horários de ônibus que fazem viagens para as diversas cidades do Estado, escreva um programa que possibilite a localização dos horários de saída e de chegada quando se forneça o destino.
'''

def pesquisa_sequencial_destino(destino, lista_horarios):
    """Retorna a lista de horários para o destino usando pesquisa sequencial, ou -1 se não encontrar."""
    resultados = []  # Lista para armazenar os resultados encontrados
    posicao = 0  # A posição inicial do índice (inicia na primeira posição)
    
    # Laço que percorre a lista de horários
    while posicao < len(lista_horarios):
        # Verifica se o destino atual da posição na lista é igual ao destino procurado
        if destino.lower() == lista_horarios[posicao]['destino'].lower():
            resultados.append(lista_horarios[posicao])  # Se for igual, adiciona o horário aos resultados
        
        posicao += 1  # Avança para o próximo item da lista
    
    # Se encontrou resultados, retorna a lista de horários encontrados
    # Caso contrário, retorna -1 indicando que não encontrou nenhum horário
    return resultados if resultados else -1


def main():
    while True:
        # Lista de destinos (para exibir ao usuário)
        cidades = ["São Paulo", "Campinas", "Rio de Janeiro"]

        # Lista de horários detalhada (com saída e chegada)
        horarios = [
            {"destino": "São Paulo", "saida": "08:00", "chegada": "12:00"},
            {"destino": "Campinas", "saida": "09:00", "chegada": "13:30"},
            {"destino": "São Paulo", "saida": "15:00", "chegada": "19:00"},
            {"destino": "Rio de Janeiro", "saida": "14:00", "chegada": "22:00"},
            {"destino": "Campinas", "saida": "07:30", "chegada": "10:30"},
        ]

        print("Destinos disponíveis:")
        for cidade in cidades:
            print(f"- {cidade}")

        destino = input("\nDigite o destino para localizar os horários: ")
        
        horarios_encontrados = pesquisa_sequencial_destino(destino, horarios)

        if horarios_encontrados != -1:
            print(f"\nHorários encontrados para o destino '{destino}':")
            for registro in horarios_encontrados:
                print(f"Saída: {registro['saida']}, Chegada: {registro['chegada']}")
        else:
            print(f"\nNenhum horário encontrado para o destino '{destino}'.")

if __name__ == "__main__":
    main()
