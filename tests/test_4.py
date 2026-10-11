import unittest
from datetime import datetime, timezone, timedelta
from src.models import Customer, Order, Item, PromoCode
from src.discounts import apply_promotional_discount

class Test4(unittest.TestCase):
    def test_promo_simulation(self):
        customer = Customer(customer_id="c-404", name="Bruce Wayne", tier="PLATINUM", email="bruce@wayne.com")
        original_price = 100.0
        item = Item(sku="TECH-01", name="Wireless Headset", price=original_price, quantity=1)
        order = Order(order_id="ord-sim-test", customer=customer, items=[item])

        now = datetime.now(timezone.utc)
        promo = PromoCode(
            code="SAVE20",
            discount_percent=0.20,
            starts_at=now - timedelta(days=1),
            expires_at=now + timedelta(days=1),
        )

        simulated_order = apply_promotional_discount(order, promo)

        self.assertEqual(simulated_order.items[0].price, 80.0)
        self.assertEqual(order.items[0].price, original_price)

if __name__ == "__main__":
    unittest.main()
