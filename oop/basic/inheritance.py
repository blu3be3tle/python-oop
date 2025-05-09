class Gadget:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f'Running device: {self.brand}'


class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory

    def coding(self):
        return f'Learning Python and practicing'


class Phone:
    def __init__(self, dual_sim):
        self.dual_sim = dual_sim

    def call(self, number, text):
        return f'Sending text to {number} with {text}'


my_phone = Phone('iphone', 120000, 'silver', 'china', True)
my_phone.phone_call()
print(my_phone.brand)
print(my_phone)