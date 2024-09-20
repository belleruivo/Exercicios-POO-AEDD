'''
Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a exercícios sobre o mesmo assunto
até que ele alcance a nota máxima (100 pontos), para só então passar ao assunto seguinte. 
Entretanto, se após 5 tentativas no mesmo nível o aluno obtiver menos de 300 pontos acumulados ele retorna
ao nível anterior. Caso contrário, ele permanece no mesmo nível, zerando novamente os pontos acumulados. 

Faça um programa que compute o progresso do aluno, através da leitura de suas notas até que ele termine o 10o nível. 
Utilize o comando break (por exemplo, para passar ao próximo nível e recomeçar quando o aluno tiver tirado a nota máxima).
'''

def progresso_do_aluno():
    num_niveis = 10
    
    nivel_atual = 1
    
    while nivel_atual <= num_niveis:
        pontos_acumulados = 0
        tentativas = 0
        
        print(f"Nível {nivel_atual}")
        
        while tentativas < 5:
            try:
                nota = int(input("Digite a nota obtida (0 a 100): "))
                
                if nota < 0 or nota > 100:
                    print("Nota inválida. Digite uma nota entre 0 e 100.")
                    continue
                
                pontos_acumulados += nota
                tentativas += 1
                
                if nota == 100:
                    print("Nota máxima atingida! Avançando para o próximo nível.")
                    nivel_atual += 1
                    break
                
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a nota.")
        
        if pontos_acumulados < 300 and tentativas >= 5:
            if nivel_atual > 1:
                print(f"Menos de 300 pontos acumulados. Retornando ao nível {nivel_atual - 1}.")
                nivel_atual -= 1
            else:
                print("Você está no primeiro nível e não pode retornar.")
        
        print() 

def main():
    print("="*30),
    print("Sistema de Ensino Experimental")
    print("="*30)
    progresso_do_aluno()
    print("Parabéns! Você completou todos os níveis.")

main()
