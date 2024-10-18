# Crie uma classe chamada Invoice que possa ser utilizado por uma loja de
# suprimentos de informática para representar uma fatura de um item vendido na loja.
# Uma fatura deve incluir as seguintes informações como atributos:
# • o número do item faturado,
# • a descrição do item,
# • a quantidade comprada do item e
# • o preço unitário do item.
# Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade
# não for positiva, ela deve ser configurada como 0. Se o preço por item não for
# positivo ele deve ser configurado como 0.0. Forneça um método set e um método get
# para cada variável de instância. Além disso, forneça um método chamado que calcula
# o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna
# o valor real. Escreva um aplicativo de teste que demonstra as capacidades da classe
# Invoice.
from fatura import Fatura
from faturaComDesconto import FaturaComDesconto

print("-" * 30)
print("     LOJA DE INFORMÁTICA")
print("-" * 30)

def main():
    numFatura = input("Digite o número da fatura: ")
    descricao = input("Digite a descrição do item: ")
    quantidade = int(input("Digite a quantidade: "))
    precoItem = float(input("Digite o preço por item: "))

    tipo_fatura = input("Digite 'normal' para fatura normal ou 'desconto' para fatura com desconto: ").strip().lower()

    if tipo_fatura == 'desconto':
        desconto = float(input("Digite o desconto em percentual: "))
        fatura = FaturaComDesconto(numFatura, descricao, quantidade, precoItem, desconto)
    else:
        fatura = Fatura(numFatura, descricao, quantidade, precoItem)

    print("-" * 30)
    print("       FATURA")
    print("-" * 30)
    print(fatura)

    nova_quantidade = int(input("\nDigite uma nova quantidade (ou 0 para sair): "))
    if nova_quantidade > 0:
        fatura.quantidade = nova_quantidade 

    novo_preco = float(input("Digite um novo preço por item (ou 0 para sair): "))
    if novo_preco > 0:
        fatura.precoItem = novo_preco

    print("\nFatura ajustada:")
    print(fatura)

main()
