'''9. Crie uma classe chamada Invoice que possa ser utilizado por uma loja de
suprimentos de informática para representar uma fatura de um item vendido na loja.
Uma fatura deve incluir as seguintes informações como atributos:
• o número do item faturado,
• a descrição do item,
• a quantidade comprada do item e
• o preço unitário do item.
Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade
não for positiva, ela deve ser configurada como 0. Se o preço por item não for
positivo ele deve ser configurado como 0.0. Forneça um método set e um método get
para cada variável de instância. Além disso, forneça um método chamado que calcula
o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna
o valor real. Escreva um aplicativo de teste que demonstra as capacidades da classe
Invoice.'''

class Fatura:
    def __init__(self, numero_item, descricao, quantidade, preco_unitario):
        self.numero_item = numero_item
        self.descricao = descricao
        self.quantidade = max(0, quantidade)  
        self.preco_unitario = max(0.0, preco_unitario) 

    
    def get_numero_item(self):
        return self.numero_item

    def get_descricao(self):
        return self.descricao

    def get_quantidade(self):
        return self.quantidade

    def get_preco_unitario(self):
        return self.preco_unitario

    
    def set_numero_item(self, numero_item):
        self.numero_item = numero_item

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_quantidade(self, quantidade):
        self.quantidade = max(0, quantidade)

    def set_preco_unitario(self, preco_unitario):
        self.preco_unitario = max(0.0, preco_unitario)

    def calcular_valor_fatura(self):
        return self.quantidade * self.preco_unitario

def obter_entrada(mensagem, tipo=float):
    while True:
        try:
            if tipo == int:
                return int(input(mensagem))
            else:
                return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico.\n")


def main():
    faturas = []  
    total_faturas = 0

    print("-="*30)
    while True:
        numero_item = obter_entrada("Digite o número do item: ", tipo=int)
        descricao = input("Digite a descrição do item: ")
        quantidade = obter_entrada("Digite a quantidade comprada: ", tipo=int)
        preco_unitario = obter_entrada("Digite o preço unitário: ")

        
        fatura = Fatura(numero_item, descricao, quantidade, preco_unitario)
        faturas.append(fatura)  

        total_faturas += fatura.calcular_valor_fatura()

        continuar = input("\nDeseja adicionar outro produto? (s/n): ").strip().lower()
        print()
        if continuar != 's':
            break

    
    print("\nDetalhes das faturas:")
    for fatura in faturas:
        print(f"\nNúmero do item: {fatura.numero_item}")
        print(f"Descrição do item: {fatura.descricao}")
        print(f"Quantidade comprada: {fatura.quantidade}")
        print(f"Preço unitário: {fatura.preco_unitario:.2f}")
        print(f"Valor total da fatura: {fatura.calcular_valor_fatura():.2f}")

    print(f"\nTotal de todas as faturas: {total_faturas:.2f}")
    print("-="*30)

main()
