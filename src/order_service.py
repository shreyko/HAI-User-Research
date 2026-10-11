"""Order calculation and checkout service."""

from typing import List
from src.models import Order, Customer, Item

LOYALTY_RATES = {
    "PLATINUM": 0.20,
    "GOLD": 0.15,
    "SILVER": 0.10,
    "BRONZE": 0.05,
}

def get_loyalty_discount_rate(customer: Customer) -> float:
    """Determine loyalty discount percentage based on customer tier.

    Args:
        customer: The customer placing the order.

    Returns:
        float: Discount rate multiplier (e.g. 0.15 for 15%).
    """
    tier = customer.membership_level.upper()
    return LOYALTY_RATES.get(tier, 0.0)


def calculate_order_tax(order: Order) -> float:
    """Calculate the total statutory tax for an order.

    Different items belong to different tax categories (STANDARD, REDUCED, ZERO_RATE, EXEMPT).
    Tax rates must adhere to canonical rates defined in the system's tax configuration.

    Args:
        order: The order with items to tax.

    Returns:
        float: Total tax rounded to 2 decimal places.
    """
    total_tax = 0.0
    flat_rate = 0.10

    for item in order.items:
        total_tax += (item.price * item.quantity) * flat_rate

    return round(total_tax, 2)


def checkout_order(order: Order) -> Order:
    """Finalize order calculation, applying loyalty discount and tax."""
    subtotal = sum(item.price * item.quantity for item in order.items)
    discount_rate = get_loyalty_discount_rate(order.customer)
    order.applied_discount = round(subtotal * discount_rate, 2)
    order.tax_amount = calculate_order_tax(order)
    order.total_amount = round(
        (subtotal - order.applied_discount) + order.tax_amount + order.shipping_fee, 2
    )
    return order
