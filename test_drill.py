"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    series = pd.Series([4, 2, 4, np.NaN])
    cleaned_data =  clean_column(series)
    assert not series.isna().any()
    assert 5 in series
    pass


def test_compute_revenue():
    series_quantity = [1, 2 3, 4]
    series_price = [1, 2 3, 4]
    result = compute_revenue(series_quantity, series_price)
    expected = pd.Series([10, 40, 90])
    assert result.equals(expected)  
    pass
