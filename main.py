"""
=====================================================================
                    RESTAURANT BILLING SYSTEM
=====================================================================
Entry point. Run this file to start the application:

    python main.py

Project Team (4 Members):
    Abhay - Menu Design & Display Module      (menu.py)
    Mokshit - Order Taking & Cart Management     (order.py)
    Tanveer - Bill Calculation & Discount Module (billing.py)
    Joel  - Receipt Generation & Testing       (receipt.py)

Final Year Python Project
=====================================================================
"""

from billing_system import RestaurantBillingSystem


def main():
    system = RestaurantBillingSystem()
    system.run()


if __name__ == "__main__":
    main()
