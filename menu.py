MENU = {
    1: ("Burger", 80),
    2: ("Pizza", 150),
    3: ("Fried Chicken", 120),
    4: ("Spaghetti", 100),
    5: ("Soft Drinks", 50),
}


def show_menu():
    print("\n------------- MENU -------------")
    for number, (name, price) in MENU.items():
        print(f"{number}. {name:<14} - PHP {price}")
    print("--------------------------------")