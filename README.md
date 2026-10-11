# OrderFlow Core Service

Welcome to the **OrderFlow Core Service** engineering session.

OrderFlow is a core service responsible for calculating order totals, statutory taxes, promotional discounts, and handling internal audit events.

Our CI/CD pipeline recently flagged failing tests in our suite. Your objective is to investigate and resolve these failures.

---

## Quick Start

### 1. Requirements
* Python 3.10+ (Standard library only; zero external dependencies required)
* Optional: `pytest`

### 2. Running Tests
You can run the entire test suite or target individual test modules:

```bash
# Run all tests
python run_tests.py

# Run an individual test suite
python run_tests.py 1
python run_tests.py 2
python run_tests.py 3
python run_tests.py 4
python run_tests.py 5
```

*(You can also use `pytest tests/` if pytest is installed in your environment).*

---

## Project Structure

```text
├── src/
│   ├── models.py           # Data models: Customer, Item, Order, PromoCode, AuditEvent
│   ├── tax_config.py       # Regional tax rate definitions
│   ├── discounts.py        # Promotional campaign evaluation & discount logic
│   ├── order_service.py    # Order checkout, loyalty discounts, and tax computation
│   └── event_queue.py      # Event queue batch processor and retry management
├── tests/
│   ├── test_1.py
│   ├── test_2.py
│   ├── test_3.py
│   ├── test_4.py
│   └── test_5.py
├── run_tests.py            # Test runner
└── requirements.txt        # Optional dependencies
```

---

## Tasks (Failing Tests)

* **Task 1 (`tests/test_1.py`):** Unhandled exception when finalizing checkout with loyalty tiers.
* **Task 2 (`tests/test_2.py`):** Discrepancy in calculated tax totals on multi-item orders.
* **Task 3 (`tests/test_3.py`):** Incomplete batch processing of queued events.
* **Task 4 (`tests/test_4.py`):** Promo discount simulation causing unexpected cart price changes.
* **Task 5 (`tests/test_5.py`):** Campaign time validation failures.

---

## Guidelines
* Feel free to use your favorite IDE, extensions, and AI coding assistants.
* You may modify any files in `src/` to fix the issues.
* Test files in `tests/` define system specifications and should remain unchanged.
