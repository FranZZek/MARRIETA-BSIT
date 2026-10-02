from menu import MENU


def get_order():
    choice = int(input("\nEnter your order (1-5): "))
    quantity = int(input("Enter quantity: "))
    return choice, quantity


def get_total(choice, quantity):
    if choice in MENU:
        name, price = MENU[choice]
        print(f"You ordered {name}.")
        return price * quantity

    print("Invalid choice!")
    return 0
class Order:
    MENU = {
        1: ("Burger", 80),
        2: ("Pizza", 150),
        3: ("Fried Chicken", 120),
        4: ("Spaghetti", 100),
        5: ("Soft Drinks", 50),
    }

    def __init__(self):
        self.choice = 0
        self.quantity = 0
        self.total = 0
        self.payment = 0

    def show_menu(self):
        print("\n------------- MENU -------------")
        for number, (name, price) in self.MENU.items():
            print(f"{number}. {name:<14} - PHP {price}")
        print("--------------------------------")

    def get_order(self):
        self.choice = int(input("\nEnter your order (1-5): "))
        self.quantity = int(input("Enter quantity: "))

    def calculate_total(self):
        if self.choice in self.MENU:
            name, price = self.MENU[self.choice]
            self.total = price * self.quantity
            print(f"You ordered {name}.")
        else:
            self.total = 0
            print("Invalid choice!")

    def display_summary(self):
        print("\n===================================")
        print("          ORDER SUMMARY")
        print("===================================")
        print("Total Amount: PHP", self.total)

    def get_payment(self):
        self.payment = float(input("Enter payment: PHP "))

    def process_payment(self):
        if self.payment >= self.total:
            change = self.payment - self.total
            print("Payment: PHP", self.payment)
            print("Change: PHP", change)

            print("\n===================================")
            print("   THANK YOU FOR YOUR ORDER!")
            print("       PLEASE COME AGAIN!")
            print("===================================")
        else:
            balance = self.total - self.payment
            print("Insufficient payment!")
            print("Remaining Balance: PHP", balance)