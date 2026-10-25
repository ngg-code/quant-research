import numpy as np
import pandas as pd
import pytest

from qresearch.metrics.returns import log_returns, simple_returns


def test_constant_price_has_zero_returns():
    prices = pd.Series([100.0, 100.0, 100.0, 100.0])
    assert (simple_returns(prices) == 0).all()
    assert np.allclose(log_returns(prices), 0)


def test_known_ten_percent_gain():
    prices = pd.Series([100.0, 110.0])
    assert simple_returns(prices).iloc[0] == pytest.approx(0.10)
    assert log_returns(prices).iloc[0] == pytest.approx(np.log(1.10))