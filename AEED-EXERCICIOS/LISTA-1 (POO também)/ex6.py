'''
Um dado material radioativo perde metade de sua massa a cada 50s. Dada a massa
inicial em gramas, fazer um algoritmo que determine o tempo necessário para que
essa massa seja menor que 0,5g.
'''

def tempo_05g(massa_inicial):
    tempo = 0
    massa = massa_inicial
    tempo_decaimento = 50  # Tempo para cada metade da massa

    while massa > 0.5:
        massa /= 2
        tempo += tempo_decaimento

    return tempo

def main():
    while True:
        try:
            massa_inicial = float(input("Digite a massa inicial do material em gramas: "))
            
            if massa_inicial <= 0:
                print("A massa inicial deve ser um valor positivo.")
            else:
                tempo = tempo_05g(massa_inicial)
                print(f"Tempo necessário para a massa ser menor que 0,5 g: {tempo} segundos")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

main()
