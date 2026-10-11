"""Discounts and promotional pricing engine."""

from datetime import datetime, timezone
from typing import Optional, List
from src.models import Order, PromoCode, Item

def is_promo_active(promo: PromoCode, current_time: Optional[datetime] = None) -> bool:
    """Verify whether a promotional discount code is active at the given time.

    Args:
        promo: The promotional code definition.
        current_time: Reference timestamp. If None, evaluates against the current system time.

    Returns:
        bool: True if promo is active, False otherwise.
    """
    if current_time is None:
        current_time = datetime.now()

    return promo.starts_at <= current_time <= promo.expires_at


def apply_promotional_discount(order: Order, promo: PromoCode) -> Order:
    """Simulate applying a promo code to an order, returning a simulated discounted order.

    The original order passed in must remain pristine and unmutated so that customers
    can test promo codes without corrupting their active shopping cart.

    Args:
        order: The source order.
        promo: The promo code to apply.

    Returns:
        Order: A new simulated order with adjusted item prices.
    """
    simulated_items = list(order.items)

    total_discount = 0.0
    for item in simulated_items:
        if item.price > 20.0:
            discount_amount = round(item.price * promo.discount_percent, 2)
            item.price = round(item.price - discount_amount, 2)
            total_discount += discount_amount

    simulated_order = Order(
        order_id=f"{order.order_id}-simulated",
        customer=order.customer,
        items=simulated_items,
        shipping_fee=order.shipping_fee,
        applied_discount=total_discount,
        tax_amount=order.tax_amount,
        total_amount=sum(i.price * i.quantity for i in simulated_items) + order.shipping_fee,
    )

    return simulated_order
