''' 2. Faça um programa que leia um conjunto de números positivos, sendo o conjunto destes números finalizado
quando for digitado um número negativo. Ao final, imprima o maior e o menor número lido e a média deles.'''

conjunto = []
print("-="*40)
print("Digite números positivos ou um negativo somente caso queira finalizar o programa.\n")


while True:
    entrada = input("Insira um número: ")
    if entrada == "":
        print("Nenhum número foi inserido. Por favor, insira um número válido.")
        continue

    try: 
        n = float(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")        
        continue

    if n < 0:
        break
    else:
        conjunto.append(n)
    
if conjunto:   
    maior = max(conjunto)
    menor = min(conjunto)
    media = sum(conjunto) / len(conjunto)

    print(f"\nOs números inseridos foram: {conjunto}")
    print(f"Menor número: {menor}") 
    print(f"Maior núnero: {maior}")      
    print(f"A média dos números inseridos: {media}") 
else:
    print("\nNenhum número foi digitado")

print("-="*40)
      