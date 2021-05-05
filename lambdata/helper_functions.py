"""Helper Functions"""

import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split


# I think this is a more scalable solution
class WrangledDataFrame:
    
    def __init__(self, my_df):
        self.df = my_df
    
    def null_count(self):
        """Counts null values"""
        return self.df.isnull().sum().sum()

    def train_test_split(self, frac):
        """Splits DF into train & test sets"""
        mask = round(len(self.df) * frac)
        train, test = self.df[:mask], self.df[mask:]
        return (train, test)

    def list_2_series(self, list_2_series):
        """Adds Series as a new column to DF"""
        col = pd.Series(list_2_series)
        self.df['new_col'] = col
        return self.df

        
# class MyDataFrame(pd.DataFrame):
#     # def __init__(self, null, split, newcol):
#     #     self.null = null
#     #     self.split = split
#     #     self.newcol = newcol
    
#     def null_count(self):
#         """Counts null values"""
#         return self.isnull().sum().sum()

#     def train_test_split(self, frac):
#         mask = round(len(self) * frac)
#         train, test = self[:mask], self[mask:]
#         return (train, test)

#     def list_2_series(self, list_2_series):
#         col = pd.Series(list_2_series)
#         self['new_col'] = col
#         return self


