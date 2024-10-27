class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name}: {self.phone_number}"

    @staticmethod
    def is_valid_phone(phone_number):
        return phone_number.isdigit() and (len(phone_number) == 8 or len(phone_number) == 9 or len(phone_number) == 11)
