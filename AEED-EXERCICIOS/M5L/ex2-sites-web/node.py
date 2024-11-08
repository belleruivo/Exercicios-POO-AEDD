'''
2. Considere uma coleção de nomes de sites da web e seus respectivos links na Internet
armazenados através de uma lista simplesmente encadeada. Escreva a respectiva
estrutura e um método que, dado o nome de um site, busque o seu link
correspondente na lista e ao mesmo tempo mova o nó que contém o nome buscado
para o início da lista, de forma que ele possa ser encontrado mais rapidamente na
próxima vez que for buscado.
'''

class Node:
    def __init__(self, site_name, link):
        self.site_name = site_name  # nome do site
        self.link = link  # link do site
        self.next = None  # próximo nó

    def __repr__(self):
        return f"Node(site_name='{self.site_name}', link='{self.link}')"
