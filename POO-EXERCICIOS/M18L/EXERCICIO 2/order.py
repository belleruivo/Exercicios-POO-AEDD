from item_order import ItemOrder

class Order:
    
    def __init__(self):
        self.items = []
        self.total = 0.0
    
    def addItem(self, item: ItemOrder):
        self.items.append(item)
        self.total += item.get_total()
    
    def getTotal(self):
        return self.total
