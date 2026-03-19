"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    s = pd.Series([1.0, 2.0, np.nan, 4.0, 5.0])
    result = clean_column(s)
    assert result.isna().sum() == 0, "NaN values remain after clean_column"
    # Median of [1, 2, 4, 5] is 3.0
    assert result.iloc[2] == 3.0, f"Expected median fill 3.0, got {result.iloc[2]}"


def test_compute_revenue():
    q = pd.Series([10, 20, 5])
    p = pd.Series([2.5, 3.0, 10.0])
    result = compute_revenue(q, p)
    expected = pd.Series([25.0, 60.0, 50.0])
    pd.testing.assert_series_equal(result, expected, check_names=False)

