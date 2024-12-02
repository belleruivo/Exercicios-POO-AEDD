from vip import VIP

class SuperiorStateroom(VIP):
    def __init__(self, value, additional_value, additional_cost):
        super().__init__(value, additional_value)
        self.additional_cost = additional_cost

    def get_value(self):
        return super().get_value() + self.additional_cost
