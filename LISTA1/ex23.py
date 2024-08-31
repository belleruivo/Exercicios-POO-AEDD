'''
23. Em um cinema que possui capacidade de 50 lugares foi distribuído um questionário
aos expectadores, no qual constava a idade e a sua opinião em relação ao filme,
segundo: ótimo, bom, regular, ruim ou péssimo. Elabore um programa que, lendo
estes dados, de diversos espectadores (até o limite de capacidade do cinema) calcule
e imprima:
a. A quantidade de respostas ótimo, bom, regular, ruim e péssimo.
b. A percentagem de ótimo, bom, regular, ruim e péssimo.
c. A idade do mais velho entrevistado.
d. A idade do mais novo entrevistado.
'''

def main(capacidade):
    num = []
    opiniao = []
    
    print("-="*10, "BEM VINDO AO MENU DE AVALIAÇÕES", "-="*10, "\n")
    print("Por favor digite sua idade e o número correspondente a sua avaliação:")
    print("""(1) - Ótimo; 
(2) - Bom; 
(3) - Regular; 
(4) - Ruim; 
(5) - Péssimo;""")
    
    for c in range(0,capacidade):
        while True:
            try:
                idade = int(input("\nQuantos anos você tem?: "))
                num.append(idade)
                break  
            except ValueError:
                print("Por favor, insira um número inteiro válido para a idade.")
        while True:
            try:
                opç = int(input("Qual a sua opinião sobre o filme? (Escolha uma das opções: 1, 2, 3, 4, 5): "))
                if opç in [1, 2, 3, 4, 5]:
                    opiniao.append(opç)
                    break  
                else:
                    print("\nPor favor, escolha uma opção válida (1, 2, 3, 4, 5).")
            except ValueError:
                print("Por favor, insira um número inteiro válido para a opinião.\n")
    
    otimo = opiniao.count(1)
    bom = opiniao.count(2)
    regular = opiniao.count(3)
    ruim = opiniao.count(4)
    pessimo = opiniao.count(5)
    
    porcentagem_1 = (otimo*100)/capacidade
    porcentagem_2 = (bom*100)/capacidade
    porcentagem_3 = (regular*100)/capacidade
    porcentagem_4 = (ruim*100)/capacidade
    porcentagem_5 = (pessimo*100)/capacidade
    
    print()
    print("-="*15, "RESULTADOS", "-="*16, "\n")
    print(f"""Quantidade e porcentagem de respostas: 
Ótimo:      {otimo:<5} {porcentagem_1:.1f}%
Bom:        {bom:<5} {porcentagem_2:.1f}%
Regular:    {regular:<5} {porcentagem_3:.1f}%
Ruim:       {ruim:<5} {porcentagem_4:.1f}%
Péssimo:    {pessimo:<5} {porcentagem_5:.1f}%""")
    
    print(f"\nA idade da pessoa mais velha: {max(num)}")
    print(f"A idade da pessoa mais nova: {min(num)}\n")
    print("-="*37)

main(50)