# Escreva um algoritmo que receba um vetor ordenado e um número extra e insira esse
# número na sua posição correta no vetor ordenado, deslocando os outros números, se
# necessário. Qual é a complexidade no melhor e no pior caso deste algoritmo?


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


# MELHOR CASO => Se o numeroExtra for maior que todos os elementos do vetor, será adicionado no fim. Nesse caso, o laço while
# será percorrido apenas uma vez para comparar com o maior elemento, e o insert() 
# será executado em tempo constante O(1)O(1) Ele realizou apenas uma operação.

# PIOR CASO: No pior cenário, o numeroExtra será menor que todos os elementos do vetor, 
# o que significa que o algoritmo terá que percorrer todo o vetor para encontrar a posição e, em seguida, 
# deslocar todos os elementos para abrir espaço. Isso faz com que a complexidade no pior caso seja O(𝑛)O(n)
# onde n é o tamanho do vetor, já que é preciso percorrer e deslocar os elementos para a direita.