'''
Do fragmento de código abaixo, determine a complexidade:
'''
s = 0  # Inicializa a variável s com zero

# Loop externo que percorre de 0 até n-2
for i = 0 to n-2:  # i vai de 0 até n-2
    # Loop intermediário que começa em i+1 e vai até n-1
    for j = i+1 to n-1:  # j vai de i+1 até n-1
        # Loop interno que começa em 1 e vai até j-1
        for k = 1 to j-1:  # k vai de 1 até j-1
            s = 1  # Atribuição constante

