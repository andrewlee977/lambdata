"""
Basic Unit testing for helper_functions.py
"""

import random
import pandas as pd
import numpy as np
import pytest
from helper_functions import WrangledDataFrame


df = pd.DataFrame(
    np.random.randint(0, 100, size=(100, 4)),
    columns=list('ABCD'))

def test_null_count():
    """
    testing null count is zero
    """
    wrangled_df = WrangledDataFrame(df)
    assert wrangled_df.null_count == 0

# def test_null_count_matches():
#     wrangled_df = WrangledDataFrame(df)
#     with pytest.raises(InsufficientAmount):
#         wrangled_df.null_count()
