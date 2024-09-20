'''
4. Uma estratégia alternativa para a função expo usa a seguinte definição recursiva:

expo(número, expoente)

= 1, quando expoente = 0.
= número * expo(número, expoente – 1), quando o expoente é ímpar.
= (expo(número, expoente / 2))2, quando o expoente é par.

Defina uma função recursiva expo que usa essa estratégia e indique sua
complexidade computacional usando a notação big-O.
'''

def expo(numero, expoente):
    if expoente == 0:
        return 1
    elif expoente % 2 == 1:  
        # função chama a si mesma, diminuindo o expoente tornando-o par 
        #--> expo(2, 3) 
        # retorna 2 * 4 = 8.
        return numero * expo(numero, expoente - 1) 
    else:  # expoente par
        metade_potencia = expo(numero, expoente // 2)
        return metade_potencia * metade_potencia # 
    
# alguns exemplos de uso da função expo
print(expo(2, 3))  # return 2 * expo(2, 2)

# A quarta chamada retornou 1 para expo(2, 0).


# a complexidade computacional desta função é O(log n), onde n é o expoente.
# cada vez que o expoente é par, ele é dividido pela metade (ou seja, expoente // 2), fazendo com que o número de chamadas da função diminua rapidamente.