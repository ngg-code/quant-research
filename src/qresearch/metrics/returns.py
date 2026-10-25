"""return calcualtions from price series"""

import numpy as np
import pandas as pd


def simple_returns(prices: pd.Series) -> pd.Series:
    """simple returns P_t / P_t-1 -1. The first (undefined) value is dropped."""
    return prices.pct_change().dropna()

def log_returns(prices: pd.Series) -> pd.Series:
    """log returns log(P_t / P_t-1). The first (undefined) value is dropped."""
    return np.log(prices).diff().dropna()