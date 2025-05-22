from abc import ABC

# users


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
        self.balance = 0
        self.order_history = []

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def place_order(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded")
            else:
                cost = item.price * quantity
                if self.balance >= cost:
                    self.balance -= cost
                    item.quantity -= quantity
                    order_item = FoodItem(item.name, item.price, quantity)
                    self.cart.place_order(order_item)
                    self.order_history.append((order_item, quantity, cost))
                    print('Order placed')
                else:
                    print("Insufficient balance")
        else:
            print('Item not found')

    def view_past_orders(self):
        print('--- Past Orders ---')
        print("Name\tQuantity\tTotal Price")
        for item, quantity, total in self.order_history:
            print(f"{item.name}\t{quantity}\t{total}")

    def check_balance(self):
        print(f'Your current balance is {self.balance}')

    def add_balance(self, amount):
        self.balance += amount
        print(f'Balance of {amount} Taka successfully added')


class Order:
    def __init__(self):
        self.items = {}

    def place_order(self, item):
        key = (item.name, item.price)
        if key in self.items:
            self.items[key] += item.quantity
        else:
            self.items[key] = item.quantity

    @property
    def total_price(self):
        return sum(name_price[1]*quantity for name_price, quantity in self.items.items())


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_customer(self, restaurant, customer):
        restaurant.add_customer(customer)

    def view_customer(self, restaurant):
        restaurant.view_customer()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def remove_customer(self, restaurant, customer_name):
        restaurant.remove_customer(customer_name)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.menu = Menu()

    def add_customer(self, customer):
        self.customers.append(customer)
        print('Customer added')

    def view_customer(self):
        print('Customer list:')
        print("Name\tEmail\tPhone\tAddress")
        for customer in self.customers:
            print(
                f"{customer.name}\t{customer.email}\t{customer.phone}\t{customer.address}")

    def find_customer(self, customer_name):
        for customer in self.customers:
            if customer.name.lower() == customer_name.lower():
                return customer
        return None

    def remove_customer(self, customer_name):
        customer = self.find_customer(customer_name)
        if customer:
            self.customers.remove(customer)
            print("Customer removed")
        else:
            print("Customer not found")


class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)
        print('Item added')

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    def show_menu(self):
        print("----- Menu -----")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


res = Restaurant('Kakar Restora')


def customer_menu():
    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    customer = Customer(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"Welcome, {customer.name}!")
        print("1. View menu")
        print("2. Place an order")
        print("3. Check balance")
        print("4. Add balance")
        print("5. View past orders")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(res)

        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.place_order(res, item_name, item_quantity)

        elif choice == 3:
            customer.check_balance()

        elif choice == 4:
            amount = int(input('Enter amount: '))
            customer.add_balance(amount)

        elif choice == 5:
            customer.view_past_orders()

        elif choice == 6:
            break

        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    admin = Admin(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"Welcome, {admin.name}!")
        print("1. Add a new item")
        print("2. Add a new customer")
        print("3. View customers")
        print("4. View items")
        print("5. Remove an item")
        print("6. Remove a customer")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(res, item)

        elif choice == 2:
            name = input("Enter customer's name: ")
            phone = input("Enter customer's phone: ")
            email = input("Enter customer's email: ")
            address = input("Enter customer's address: ")
            customer = Customer(name=name, phone=phone,
                                email=email, address=address)
            admin.add_customer(res, customer)

        elif choice == 3:
            admin.view_customer(res)

        elif choice == 4:
            admin.view_menu(res)

        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(res, item_name)

        elif choice == 6:
            customer_name = input("Enter customer's name: ")
            admin.remove_customer(res, customer_name)

        elif choice == 7:
            break

        else:
            print("Invalid Input")


while True:
    print("Welcome!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_menu()

    elif choice == 2:
        admin_menu()

    elif choice == 3:
        break

    else:
        print("Invalid input!")
