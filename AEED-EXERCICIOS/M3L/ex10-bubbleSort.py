'''
Faça um programa que cadastre n números, ordene-os pelo bubbleSort e em seguida encontre e mostre:
a. O menor número e quantas vezes ele aparece no vetor.
b. O maior número e quantas vezes ele aparece no vetor.
'''

def bubbleSort(lst):
    """Ordena o vetor usando o algoritmo Bubble Sort com melhoria (tweak)."""
    n = len(lst)  # Tamanho da lista
    while n > 1:  # Enquanto houver elementos para comparar
        swapped = False  # Flag para verificar se houve troca
        i = 1  # Começa a comparar da segunda posição
        while i < n:
            if lst[i] < lst[i-1]:  # Se o elemento atual for menor que o anterior
                # Troca os elementos
                lst[i], lst[i-1] = lst[i-1], lst[i]
                swapped = True  # Marca que houve uma troca
            i += 1
        # Se não houve troca, a lista já está ordenada
        if not swapped:
            return
        # Reduz o limite da próxima iteração, pois o maior elemento já está no final
        n -= 1

def contar_ocorrencias(vetor, numero):
    """Conta quantas vezes o número aparece no vetor."""
    return vetor.count(numero)

def main():
    n = int(input("Quantos números você deseja cadastrar? "))
    
    numeros = []
    for i in range(n):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    
    bubbleSort(numeros)
    
    print("\nLista ordenada:", numeros)
    
    menor_numero = numeros[0]
    vezes_menor = contar_ocorrencias(numeros, menor_numero)
    
    maior_numero = numeros[-1]
    vezes_maior = contar_ocorrencias(numeros, maior_numero)
    
    print(f"\nO menor número é {menor_numero} e ele aparece {vezes_menor} vez(es).")
    print(f"O maior número é {maior_numero} e ele aparece {vezes_maior} vez(es).")

if __name__ == "__main__":
    main()
