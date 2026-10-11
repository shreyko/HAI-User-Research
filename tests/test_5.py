import unittest
from datetime import datetime, timezone, timedelta
from src.models import PromoCode
from src.discounts import is_promo_active

class Test5(unittest.TestCase):
    def test_default_evaluation(self):
        now_utc = datetime.now(timezone.utc)
        promo = PromoCode(
            code="SPRING2026",
            discount_percent=0.15,
            starts_at=now_utc - timedelta(hours=2),
            expires_at=now_utc + timedelta(hours=2),
        )

        active = is_promo_active(promo)
        self.assertTrue(active)

    def test_time_boundaries(self):
        edt_tz = timezone(timedelta(hours=-4))

        promo_start_utc = datetime(2026, 10, 15, 10, 0, 0, tzinfo=timezone.utc)
        promo_end_utc = datetime(2026, 10, 15, 18, 0, 0, tzinfo=timezone.utc)

        promo = PromoCode(
            code="FLASHSALE",
            discount_percent=0.30,
            starts_at=promo_start_utc,
            expires_at=promo_end_utc,
        )

        expired_edt_time = datetime(2026, 10, 15, 14, 30, 0, tzinfo=edt_tz)
        self.assertFalse(is_promo_active(promo, current_time=expired_edt_time))

        valid_edt_time = datetime(2026, 10, 15, 13, 30, 0, tzinfo=edt_tz)
        self.assertTrue(is_promo_active(promo, current_time=valid_edt_time))

if __name__ == "__main__":
    unittest.main()
