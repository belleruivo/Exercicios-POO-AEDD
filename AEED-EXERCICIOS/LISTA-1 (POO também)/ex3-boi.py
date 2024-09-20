'''
Em um frigorífico, cada boi é identificado por um cartão que contém seu número e seu peso. Faça um programa que leia os números de identificação e o peso de cada boi e ao final imprima o número de identificação e o peso do boi mais gordo, do boi mais magro e o total de peso dos bois do frigorífico.
'''

def main():
    bois = {}  
    total_peso = 0
    i = 0
    while True:
        try:
            identificacao = input(f"Digite o número de identificação do boi {i + 1}° (ou 'sair' para finalizar): ")
            if identificacao.lower() == 'sair':
                break
            
            # Verifica se a identificação contém apenas números
            if not identificacao.isdigit():
                print("A identificação deve conter apenas números. Tente novamente.")
                continue
            
            # Verifica se a identificação já foi registrada
            if identificacao in bois:
                print("Essa identificação já foi registrada. Tente novamente.")
                continue
            
            peso = float(input("Digite o peso do boi (em kg): "))
            
            # Verifica se o peso é positivo
            if peso <= 0:
                print("O peso deve ser um valor positivo. Tente novamente.")
                continue
            
            bois[identificacao] = peso
            total_peso += peso  
            i += 1  # Incrementa o contador apenas se a entrada for válida

        except ValueError:
            print("Por favor, digite um valor numérico válido para o peso.")

    if bois:
        # O argumento key é uma função que especifica um critério para comparação.
        boi_mais_gordo = max(bois, key=bois.get) 
        boi_mais_magro = min(bois, key=bois.get)

        print(f"\nBoi mais gordo: ID {boi_mais_gordo}, Peso {bois[boi_mais_gordo]:.2f} kg")
        print(f"Boi mais magro: ID {boi_mais_magro}, Peso {bois[boi_mais_magro]:.2f} kg")
        print(f"Peso total dos bois: {total_peso:.2f} kg")
    else:
        print("Nenhum boi foi registrado.")

main()
