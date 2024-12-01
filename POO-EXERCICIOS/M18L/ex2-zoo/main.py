'''
Implemente um sistema de Zoológico com sua classificação (mamífero, ave, réptil, etc.), evidenciando a classe Animal como uma classe abstrata. Por exemplo, considere a estrutura abaixo:
'''
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from alimentacao import Alimentacao
from cuidados import Cuidados

def adicionar_animal(animais):
    nome = input("Digite o nome do animal: ")
    idade = int(input("Digite a idade do animal: "))
    alimentacao_tipo = input("Digite o tipo de alimentação do animal: ")
    alimentacao_quantidade = input("Digite a quantidade de alimentação do animal: ")
    alimentacao = Alimentacao(alimentacao_tipo, alimentacao_quantidade)
    cuidados_necessidade = input("Digite a necessidade de cuidados do animal: ")
    cuidados = Cuidados(cuidados_necessidade)
    
    print("Classificações de animal: 1. Mamífero 2. Ave 3. Réptil")
    tipo = int(input("Selecione a classificação do animal (1-3): "))
    
    if tipo == 1:
        animal = Mamifero(nome, idade, alimentacao, cuidados)
    elif tipo == 2:
        animal = Ave(nome, idade, alimentacao, cuidados)
    elif tipo == 3:
        animal = Reptil(nome, idade, alimentacao, cuidados)
    else:
        print("Classificação inválida. Animal não adicionado.")
        return
    
    animais.append(animal)
    print(f'Animal {nome} adicionado com sucesso!')

def listar_animais(animais):
    if not animais:
        print("Nenhum animal registrado.")
        return
    
    for animal in animais:
        print(f'Nome: {animal.nome}, Idade: {animal.idade}, Classificação: {animal.get_classificacao()}, Som: {animal.emitir_som()}')
        print(f'Alimentação: {animal.alimentacao.get_dieta()}, Cuidados: {animal.cuidados.get_necessidade()}')

def main():
    animais = []
    
    while True:
        print("\nSistema de Gestão do Zoológico")
        print("1. Adicionar Animal")
        print("2. Listar Animais")
        print("3. Sair")
        
        opcao = int(input("Selecione uma opção (1-3): "))
        
        if opcao == 1:
            adicionar_animal(animais)
        elif opcao == 2:
            listar_animais(animais)
        elif opcao == 3:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

'''
Composição de Classes: Criamos classes componentes (Alimentacao e Cuidados) que são usadas dentro de Animal para compor suas funcionalidades.

Classes Concretas: As classes de animais (Ave, Mamifero, Reptil) usam essas classes componentes.

Sistema Interativo: O main.py foi atualizado para incluir a entrada de alimentação e cuidados ao adicionar um novo animal e exibir essas informações ao listar os animais.
'''