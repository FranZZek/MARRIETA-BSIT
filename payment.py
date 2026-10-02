def get_payment():
    return float(input("Enter payment: PHP "))


def process_payment(total, payment):
    if payment >= total:
        change = payment - total
        print("Payment: PHP", payment)
        print("Change: PHP", change)
        return True

    balance = total - payment
    print("Insufficient payment!")
    print("Remaining Balance: PHP", balance)
    return False