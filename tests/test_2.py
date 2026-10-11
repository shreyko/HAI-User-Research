import unittest
from src.models import Customer, Order, Item
from src.order_service import calculate_order_tax

class Test2(unittest.TestCase):
    def test_tax_calculation(self):
        customer = Customer(
            customer_id="c-100",
            name="Diana Prince",
            tier="SILVER",
            email="diana@example.com"
        )
        items = [
            Item(sku="ELEC-1", name="Laptop", price=1000.0, quantity=1, tax_category="STANDARD"),
            Item(sku="GROC-1", name="Organic Apples", price=20.0, quantity=2, tax_category="REDUCED"),
            Item(sku="MED-1", name="First Aid Kit", price=50.0, quantity=1, tax_category="ZERO_RATE"),
        ]
        order = Order(order_id="ord-tax-1", customer=customer, items=items)

        calculated_tax = calculate_order_tax(order)
        self.assertEqual(calculated_tax, 102.0)

if __name__ == "__main__":
    unittest.main()
