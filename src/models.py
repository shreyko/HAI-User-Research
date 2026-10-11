"""Domain data models for OrderFlow Core Service."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional

@dataclass
class Customer:
    customer_id: str
    name: str
    tier: str  # Valid tiers: "BRONZE", "SILVER", "GOLD", "PLATINUM"
    email: str

@dataclass
class Item:
    sku: str
    name: str
    price: float
    quantity: int = 1
    tax_category: str = "STANDARD"  # STANDARD, REDUCED, ZERO_RATE, EXEMPT

@dataclass
class PromoCode:
    code: str
    discount_percent: float  # e.g., 0.15 for 15%
    starts_at: datetime
    expires_at: datetime

@dataclass
class Order:
    order_id: str
    customer: Customer
    items: List[Item] = field(default_factory=list)
    shipping_fee: float = 5.0
    applied_discount: float = 0.0
    tax_amount: float = 0.0
    total_amount: float = 0.0

@dataclass
class AuditEvent:
    event_id: str
    event_type: str
    payload: Dict[str, Any]
    retry_count: int = 0
    status: str = "PENDING"  # PENDING, PROCESSED, DEAD_LETTER
