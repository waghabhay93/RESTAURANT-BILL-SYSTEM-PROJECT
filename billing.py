"""
=====================================================================
            MODULE 3: BILL CALCULATION & DISCOUNT
                        (Member 3)
=====================================================================
Handles subtotal calculation, slab/coupon-based discounts, tax and
the final grand total.
=====================================================================
"""

from config import GST_RATE


def calculate_subtotal(menu, cart):
    """Returns the subtotal (before tax/discount) of the cart."""
    return sum(menu[i].price * qty for i, qty in cart.items())


def apply_discount(subtotal, coupon_code=None):
    """
    Applies slab-based discount on the subtotal.
    Rules:
        Bill > Rs.1500          -> 15% off
        Bill > Rs.1000          -> 10% off
        Bill > Rs.500           -> 5%  off
        Coupon 'WELCOME10'      -> Flat 10% off (overrides slab if better)
    Returns: (discount_amount, discount_percent)
    """
    slab_percent = 0
    if subtotal > 1500:
        slab_percent = 15
    elif subtotal > 1000:
        slab_percent = 10
    elif subtotal > 500:
        slab_percent = 5

    coupon_percent = 10 if coupon_code and coupon_code.upper() == "WELCOME10" else 0
    final_percent = max(slab_percent, coupon_percent)
    discount_amount = (subtotal * final_percent) / 100
    return round(discount_amount, 2), final_percent


def calculate_bill(menu, cart, coupon_code=None):
    """
    Calculates the full bill breakdown.
    Returns a dictionary with subtotal, discount, tax and total.
    """
    subtotal = calculate_subtotal(menu, cart)
    discount_amount, discount_percent = apply_discount(subtotal, coupon_code)
    taxable_amount = subtotal - discount_amount
    tax_amount = round(taxable_amount * GST_RATE, 2)
    grand_total = round(taxable_amount + tax_amount, 2)

    return {
        "subtotal": round(subtotal, 2),
        "discount_percent": discount_percent,
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "grand_total": grand_total,
    }
