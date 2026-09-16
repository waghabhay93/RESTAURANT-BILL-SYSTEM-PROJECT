"""
=====================================================================
                            MODELS
=====================================================================
Data model classes for the Restaurant Billing System.
=====================================================================
"""


class MenuItem:
    """Represents a single item on the restaurant menu."""

    def __init__(self, item_id, name, category, price):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return (f"MenuItem(item_id={self.item_id!r}, name={self.name!r}, "
                f"category={self.category!r}, price={self.price!r})")
