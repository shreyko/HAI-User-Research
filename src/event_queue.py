"""Audit event queue processor with retry policy and dead letter handling."""

from typing import List, Callable
from src.models import AuditEvent

class EventQueue:
    def __init__(self, max_retries: int = 3):
        self.pending: List[AuditEvent] = []
        self.processed: List[AuditEvent] = []
        self.dead_letter: List[AuditEvent] = []
        self.max_retries = max_retries

    def enqueue(self, event: AuditEvent) -> None:
        """Add an event to the pending queue."""
        self.pending.append(event)

    def process_batch(self, handler: Callable[[AuditEvent], bool]) -> int:
        """Process all pending events in the queue using the provided handler.

        Events that succeed are marked PROCESSED and moved to self.processed.
        Events that fail have retry_count incremented. If retry_count reaches max_retries,
        they are marked DEAD_LETTER and moved to self.dead_letter. Otherwise they remain pending.

        Returns:
            int: Number of successfully processed events in this run.
        """
        success_count = 0

        for event in self.pending:
            try:
                ok = handler(event)
            except Exception:
                ok = False

            if ok:
                event.status = "PROCESSED"
                self.processed.append(event)
                self.pending.remove(event)
                success_count += 1
            else:
                event.retry_count += 1
                if event.retry_count >= self.max_retries:
                    event.status = "DEAD_LETTER"
                    self.dead_letter.append(event)
                    self.pending.remove(event)

        return success_count
