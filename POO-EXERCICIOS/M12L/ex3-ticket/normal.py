from ticket import Ticket

class Normal(Ticket):
    def __init__(self, value):
        super().__init__(value)

    def get_value(self):
        return super().get_value()
