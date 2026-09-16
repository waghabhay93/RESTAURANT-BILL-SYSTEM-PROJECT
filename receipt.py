"""
=====================================================================
            MODULE 4: RECEIPT GENERATION & TESTING
                        (Member 4)
=====================================================================
Handles printing a neatly formatted final receipt for the customer.
=====================================================================
"""

import datetime
import random

from config import (
    RESTAURANT_NAME,
    RESTAURANT_ADDRESS,
    RESTAURANT_PHONE,
    GST_RATE,
    RECEIPT_WIDTH,
)


def print_receipt(menu, cart, bill, customer_name="Guest"):
    """Prints a neatly formatted final receipt."""
    order_id = random.randint(1000, 9999)
    now = datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")

    line = "-" * RECEIPT_WIDTH
    print("\n" + "=" * RECEIPT_WIDTH)
    print(f"{RESTAURANT_NAME.upper():^{RECEIPT_WIDTH}}")
    print(f"{RESTAURANT_ADDRESS:^{RECEIPT_WIDTH}}")
    print(f"{'Ph: ' + RESTAURANT_PHONE:^{RECEIPT_WIDTH}}")
    print("=" * RECEIPT_WIDTH)
    print(f"Order ID : {order_id}")
    print(f"Customer : {customer_name}")
    print(f"Date/Time: {now}")
    print(line)
    print(f"{'Item':<20}{'Qty':>5}{'Rate':>9}{'Amount':>12}")
    print(line)

    for item_id, qty in cart.items():
        item = menu[item_id]
        amount = item.price * qty
        print(f"{item.name:<20}{qty:>5}{item.price:>9.2f}{amount:>12.2f}")

    print(line)
    print(f"{'Subtotal':<34}Rs.{bill['subtotal']:>9.2f}")
    if bill["discount_percent"] > 0:
        print(f"{'Discount (' + str(bill['discount_percent']) + '%)':<34}"
              f"-Rs.{bill['discount_amount']:>8.2f}")
    print(f"{'GST (' + str(int(GST_RATE * 100)) + '%)':<34}Rs.{bill['tax_amount']:>9.2f}")
    print(line)
    print(f"{'GRAND TOTAL':<34}Rs.{bill['grand_total']:>9.2f}")
    print("=" * RECEIPT_WIDTH)
    print("Thank you for dining with us! Visit again.".center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH + "\n")
