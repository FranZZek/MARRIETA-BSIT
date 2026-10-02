from display import show_welcome, show_summary, show_thank_you
from menu import show_menu
from order import get_order, get_total
from payment import get_payment, process_payment


def main() -> None:
    show_welcome()
    show_menu()

    choice, quantity = get_order()
    total = get_total(choice, quantity)

    show_summary(total)
    payment = get_payment()

    if process_payment(total, payment):
        show_thank_you()


if __name__ == "__main__":
    main()
