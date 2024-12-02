from vip import VIP

class LowerStateroom(VIP):
    def __init__(self, value, additional_value, location):
        super().__init__(value, additional_value)
        self.location = location

    def get_location(self):
        return self.location

    def print_location(self):
        print(f'Location: {self.location}')
