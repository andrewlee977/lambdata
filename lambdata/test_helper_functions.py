"""
Basic Unit testing for helper_functions.py
"""

import random
import pandas as pd
import numpy as np
import pytest
from lambdata import helper_functions


df = pd.DataFrame(
    np.random.randint(0, 100, size=(100, 4)),
    columns=list('ABCD'))

def test_null_count():
    """
    testing null count is zero
    """
    wrangled_df = helper_functions.WrangledDataFrame(df)
    null_count = wrangled_df.null_count()
    assert isinstance(null_count, np.int64)

# def test_null_count_matches():
#     wrangled_df = WrangledDataFrame(df)
#     with pytest.raises(InsufficientAmount):
#         wrangled_df.null_count()
