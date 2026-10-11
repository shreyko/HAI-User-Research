import unittest
from src.models import AuditEvent
from src.event_queue import EventQueue

class Test3(unittest.TestCase):
    def test_batch_processing(self):
        queue = EventQueue(max_retries=3)

        e1 = AuditEvent(event_id="evt-1", event_type="ORDER_PLACED", payload={"order_id": "101"})
        e2 = AuditEvent(event_id="evt-2", event_type="PAYMENT_CAPTURED", payload={"order_id": "101"})
        e3 = AuditEvent(event_id="evt-3", event_type="RECEIPT_EMAILED", payload={"order_id": "101"})

        queue.enqueue(e1)
        queue.enqueue(e2)
        queue.enqueue(e3)

        def mock_handler(event: AuditEvent) -> bool:
            return True

        processed_count = queue.process_batch(mock_handler)

        self.assertEqual(len(queue.pending), 0)
        self.assertEqual(processed_count, 3)
        self.assertEqual(len(queue.processed), 3)

    def test_dead_letter(self):
        queue = EventQueue(max_retries=2)

        e1 = AuditEvent(event_id="evt-fail-1", event_type="SYNC", payload={}, retry_count=1)
        e2 = AuditEvent(event_id="evt-fail-2", event_type="SYNC", payload={}, retry_count=1)

        queue.enqueue(e1)
        queue.enqueue(e2)

        queue.process_batch(lambda evt: False)

        self.assertEqual(len(queue.pending), 0)
        self.assertEqual(len(queue.dead_letter), 2)

if __name__ == "__main__":
    unittest.main()
