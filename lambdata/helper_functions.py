"""Helper Functions"""

import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

def null_count(df):
    """Counts null values"""
    return df.isnull().sum().sum()

def train_test_split(df, frac):
    mask = round(len(df) * frac)
    train, test = df[:mask], df[mask:]
    return (train, test)

def list_2_series(list_2_series, df):
    col = pd.Series(list_2_series)
    df['new_col'] = col
    return df

