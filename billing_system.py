"""
=====================================================================
                        CORE BILLING SYSTEM
=====================================================================
The RestaurantBillingSystem class is the "glue" class that connects
every module together (menu, order, billing, receipt) and drives the
main program flow. Each module keeps its own single responsibility;
this class just wires them up.
=====================================================================
"""

from menu import build_menu, display_menu
from order import take_order
from billing import calculate_bill
from receipt import print_receipt
from config import RECEIPT_WIDTH


class RestaurantBillingSystem:
    """Core class that ties together menu, orders, billing and receipts."""

    def __init__(self):
        self.menu = build_menu()
        self.cart = {}   # {item_id: quantity}

    # -----------------------------------------------------------
    # MODULE 1: MENU (Member 1)
    # -----------------------------------------------------------
    def display_menu(self):
        display_menu(self.menu)

    # -----------------------------------------------------------
    # MODULE 2: TAKE ORDER (Member 2)
    # -----------------------------------------------------------
    def take_order(self):
        take_order(self.menu, self.cart)

    # -----------------------------------------------------------
    # MODULE 3: CALCULATE BILL & DISCOUNT (Member 3)
    # -----------------------------------------------------------
    def calculate_bill(self, coupon_code=None):
        return calculate_bill(self.menu, self.cart, coupon_code)

    # -----------------------------------------------------------
    # MODULE 4: PRINT RECEIPT (Member 4)
    # -----------------------------------------------------------
    def print_receipt(self, bill, customer_name="Guest"):
        print_receipt(self.menu, self.cart, bill, customer_name)

    # -----------------------------------------------------------
    # MAIN PROGRAM FLOW
    # -----------------------------------------------------------
    def run(self):
        print("\n" + "#" * RECEIPT_WIDTH)
        print("WELCOME TO THE RESTAURANT BILLING SYSTEM".center(RECEIPT_WIDTH))
        print("#" * RECEIPT_WIDTH)

        customer_name = input("\nEnter Customer Name: ").strip() or "Guest"

        while True:
            self.display_menu()
            self.take_order()

            if self.cart:
                coupon = input(
                    "\nHave a coupon code? (Press Enter to skip): "
                ).strip()
                bill = self.calculate_bill(coupon_code=coupon if coupon else None)
                self.print_receipt(bill, customer_name)

            again = input("Start a new bill? (y/n): ").strip().lower()
            if again != "y":
                print("\nThank you for using the Restaurant Billing System!")
                break
            self.cart = {}   # reset cart for a fresh order
