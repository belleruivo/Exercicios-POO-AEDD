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
def coletar_dados(capacidade):
    idades = []
    opiniao = []
    
    print("-="*10, "BEM VINDO AO MENU DE AVALIAÇÕES", "-="*10, "\n")
    print("Por favor digite sua idade e o número correspondente a sua avaliação:")
    print("""(1) - Ótimo; 
(2) - Bom; 
(3) - Regular; 
(4) - Ruim; 
(5) - Péssimo;""")
    
    for _ in range(capacidade):
        idade = obter_idade()
        opç = obter_opiniao()
        
        idades.append(idade)
        opiniao.append(opç)
        
    return idades, opiniao

def obter_idade():
    while True:
        try:
            idade = int(input("\nQuantos anos você tem?: "))
            if 0 <= idade <= 100:
                return idade
            else:
                print("Insira uma idade válida (0 a 100).")
        except ValueError:
            print("Por favor, insira um número inteiro válido para a idade.")

def obter_opiniao():
    while True:
        try:
            opç = int(input("Qual a sua opinião sobre o filme? (Escolha uma das opções: 1, 2, 3, 4, 5): "))
            if opç in [1, 2, 3, 4, 5]:
                return opç
            else:
                print("\nPor favor, escolha uma opção válida (1, 2, 3, 4, 5).")
        except ValueError:
            print("Por favor, insira um número inteiro válido para a opinião.\n")

def calcular_estatisticas(opiniao, idades):
    estatisticas = {
        'ótimo': opiniao.count(1),
        'bom': opiniao.count(2),
        'regular': opiniao.count(3),
        'ruim': opiniao.count(4),
        'péssimo': opiniao.count(5),
    }
    
    total_respostas = len(opiniao)
    porcentagens = {key: (value * 100) / total_respostas for key, value in estatisticas.items()}
    
    return estatisticas, porcentagens, max(idades), min(idades)

def imprimir_resultados(estatisticas, porcentagens, mais_velho, mais_novo):
    print()
    print("-="*15, "RESULTADOS", "-="*16, "\n")
    print(f"""Quantidade e porcentagem de respostas: 
Ótimo:      {estatisticas['ótimo']:<5} {porcentagens['ótimo']:.1f}%
Bom:        {estatisticas['bom']:<5} {porcentagens['bom']:.1f}%
Regular:    {estatisticas['regular']:<5} {porcentagens['regular']:.1f}%
Ruim:       {estatisticas['ruim']:<5} {porcentagens['ruim']:.1f}%
Péssimo:    {estatisticas['péssimo']:<5} {porcentagens['péssimo']:.1f}%""")
    
    print(f"\nA idade da pessoa mais velha: {mais_velho}")
    print(f"A idade da pessoa mais nova: {mais_novo}\n")
    print("-="*37)

def main(capacidade):
    idades, opiniao = coletar_dados(capacidade)
    estatisticas, porcentagens, mais_velho, mais_novo = calcular_estatisticas(opiniao, idades)
    imprimir_resultados(estatisticas, porcentagens, mais_velho, mais_novo)

main(50) #podemos diminuir esse número para fazer o teste
'''
def main(capacidade):
    idades = []
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
                if idade >100 or idade <0:
                    print("Insira uma idade válida")
                else:
                    idades.append(idade)
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
    
    print(f"\nA idade da pessoa mais velha: {max(idades)}")
    print(f"A idade da pessoa mais nova: {min(idades)}\n")
    print("-="*37)

main(50) #Podemos colocar um número menor só para fazer o teste
'''