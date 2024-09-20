# Escreva um algoritmo que receba um vetor ordenado e um número extra e insira esse
# número na sua posição correta no vetor ordenado, deslocando os outros números, se
# necessário. Qual é a complexidade no melhor e no pior caso deste algoritmo?

print('-------------------------------------------------')
print('---------------------VETORES---------------------')
print('-------------------------------------------------')

def main(vetor, numeroExtra):
    #i = 0
    #while i < len(vetor) and vetor[i] < numeroExtra: #encontrar posição
    
    for i in range(len(vetor)):
        if vetor[i] >= numeroExtra:
            vetor.insert(i, numeroExtra) #Inserir em um indice anterior
            break
    if numeroExtra > vetor[i]:
        vetor.append(numeroExtra)
            

vetor = [1, 3, 5, 7, 9]
while True:
    try:
        numeroExtra = int(input("Digite um valor: "))
        break
    except ValueError:
        print("Por favor, insira um número inteiro!\n")

main(vetor, numeroExtra)
print(vetor) 


# MELHOR CASO =>  O(1)

# PIOR CASO => O(𝑛)