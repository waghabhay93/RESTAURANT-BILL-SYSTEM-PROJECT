"""
=====================================================================
            MODULE 2: ORDER TAKING & CART MANAGEMENT
                        (Member 2)
=====================================================================
Handles adding items to the cart and the interactive order-taking
loop.
=====================================================================
"""


def add_item_to_cart(menu, cart, item_id, quantity):
    """Adds a validated item + quantity to the cart."""
    if item_id not in menu:
        print(" Invalid Item ID. Please check the menu again.")
        return False
    if quantity <= 0:
        print(" Quantity must be greater than zero.")
        return False

    cart[item_id] = cart.get(item_id, 0) + quantity
    print(f" Added {quantity} x {menu[item_id].name} to your order.")
    return True


def take_order(menu, cart):
    """Interactive loop that lets the user build their order."""
    print("\n--- TAKE ORDER ---")
    print("Enter the Item ID from the menu to order.")
    print("Type 0 when you are done ordering.\n")

    while True:
        try:
            item_id = int(input("Enter Item ID (0 to finish): "))
        except ValueError:
            print(" Please enter a valid numeric Item ID.")
            continue

        if item_id == 0:
            break

        try:
            quantity = int(input("Enter Quantity: "))
        except ValueError:
            print(" Please enter a valid quantity.")
            continue

        add_item_to_cart(menu, cart, item_id, quantity)

    if not cart:
        print("\nNo items were ordered.")
