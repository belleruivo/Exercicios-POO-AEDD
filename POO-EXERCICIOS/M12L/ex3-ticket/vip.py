from ticket import Ticket

class VIP(Ticket):
    def __init__(self, value, additional_value):
        super().__init__(value)
        self.additional_value = additional_value

    def get_value(self):
        return super().get_value() + self.additional_value
