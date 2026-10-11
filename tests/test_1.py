import unittest
from src.models import Customer, Order, Item
from src.order_service import checkout_order, get_loyalty_discount_rate

class Test1(unittest.TestCase):
    def test_loyalty_discount(self):
        customer = Customer(
            customer_id="c-001",
            name="Alice Smith",
            tier="GOLD",
            email="alice@example.com"
        )
        rate = get_loyalty_discount_rate(customer)
        self.assertEqual(rate, 0.15)

    def test_checkout(self):
        customer = Customer(
            customer_id="c-002",
            name="Bob Jones",
            tier="PLATINUM",
            email="bob@example.com"
        )
        order = Order(
            order_id="ord-001",
            customer=customer,
            items=[Item(sku="SKU-1", name="Keyboard", price=100.0, quantity=1)],
            shipping_fee=5.0
        )
        finalized = checkout_order(order)
        self.assertEqual(finalized.applied_discount, 20.0)

if __name__ == "__main__":
    unittest.main()
