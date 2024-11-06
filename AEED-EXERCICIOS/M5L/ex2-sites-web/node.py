class Node:
    def __init__(self, site_name, link):
        self.site_name = site_name  # nome do site
        self.link = link  # link do site
        self.next = None  # próximo nó

    def __repr__(self):
        return f"Node(site_name='{self.site_name}', link='{self.link}')"
