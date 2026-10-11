"""Tax configuration and rate mappings for regional compliance.

This module is the canonical source of truth for all tax rates.
Different item categories carry different tax liabilities.
"""

from typing import Dict

# Canonical tax rates by tax category
TAX_RATES: Dict[str, float] = {
    "STANDARD": 0.10,    # 10% standard rate for consumer electronics, luxury
    "REDUCED": 0.05,     # 5% reduced rate for groceries, books, essentials
    "ZERO_RATE": 0.00,   # 0% medical supplies
    "EXEMPT": 0.00,      # Exempt services / donations
}

DEFAULT_TAX_RATE = 0.10

def get_tax_rate(category: str) -> float:
    """Retrieve the statutory tax rate for a given tax category.

    Args:
        category: The item tax category code.

    Returns:
        float: Tax rate decimal (e.g. 0.05 for 5%).
    """
    category_upper = category.upper() if category else "STANDARD"
    return TAX_RATES.get(category_upper, DEFAULT_TAX_RATE)
