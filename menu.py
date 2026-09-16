"""
=====================================================================
                MODULE 1: MENU DESIGN & DISPLAY
                        (Member 1)
=====================================================================
Handles building the restaurant menu and printing it in a neatly
formatted, categorized menu card.
=====================================================================
"""

from models import MenuItem
from config import RESTAURANT_NAME, RECEIPT_WIDTH


def build_menu():
    """Builds and returns the restaurant menu as a dictionary."""
    items = [
        (101, "Veg Spring Roll",       "Starters",   150),
        (102, "Paneer Tikka",          "Starters",   190),
        (103, "Chicken Wings",         "Starters",   220),
        (201, "Paneer Butter Masala",  "Main Course", 240),
        (202, "Dal Makhani",           "Main Course", 190),
        (203, "Butter Chicken",        "Main Course", 280),
        (301, "Butter Naan",           "Breads",       45),
        (302, "Tandoori Roti",         "Breads",       30),
        (401, "Veg Biryani",           "Rice",        210),
        (402, "Chicken Biryani",       "Rice",        260),
        (501, "Gulab Jamun (2 pcs)",   "Desserts",     80),
        (502, "Ice Cream Scoop",       "Desserts",     70),
        (601, "Masala Chaas",          "Beverages",    50),
        (602, "Cold Coffee",           "Beverages",    90),
    ]
    return {i[0]: MenuItem(*i) for i in items}


def display_menu(menu):
    """Prints the full menu grouped by category."""
    print("\n" + "=" * RECEIPT_WIDTH)
    print(f"{RESTAURANT_NAME.upper():^{RECEIPT_WIDTH}}")
    print("MENU CARD".center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)

    categories = sorted(set(item.category for item in menu.values()))
    for category in categories:
        print(f"\n-- {category} --")
        print(f"{'ID':<6}{'Item':<26}{'Price':>10}")
        for item in menu.values():
            if item.category == category:
                print(f"{item.item_id:<6}{item.name:<26}"
                      f"Rs.{item.price:>7.2f}")
    print("\n" + "=" * RECEIPT_WIDTH)
