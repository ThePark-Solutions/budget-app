import pytest
from summarize import total_spent

def test_total_spent_skips_paypment():
  rows = [
    {"Type": "Sale", "Amount": "-10.00"},
    {"Type": "Payment", "Amount": "50.00"},
  ]
  assert total_spent(rows) == pytest.approx(10.00)