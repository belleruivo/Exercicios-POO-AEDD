'''
O número 3025 possui a interessante característica:
30 + 25 = 55
55² = 3025
Faça um programa que procure todos os números de 4 algarismos que possuem essa
característica.
'''

def verificar_caracteristica(numero):
    """Verifica se o número possui a característica descrita."""
    str_numero = str(numero)
    parte1 = int(str_numero[:2])
    parte2 = int(str_numero[2:])
    
    soma = parte1 + parte2
    quadrado_soma = soma ** 2
    
    return quadrado_soma == numero

def encontrar_numeros_caracteristicos():
    """Encontra todos os números de 4 algarismos que possuem a característica."""
    numeros_caracteristicos = []
    
    for numero in range(1000, 10000):
        if verificar_caracteristica(numero):
            numeros_caracteristicos.append(numero)
    
    return numeros_caracteristicos

def main():
    print("Números de 4 algarismos com a característica:")
    numeros = encontrar_numeros_caracteristicos()
    
    for numero in numeros:
        print(numero)

main()
