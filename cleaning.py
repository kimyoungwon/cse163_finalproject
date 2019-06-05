# This file is the cleaning process of the data
from utils import make_colnames, gender_label
import pandas as pd
import numpy as np


class FF_wave9:

    def __init__(self, fname):
        self._fname = fname
        self._df = pd.read_csv(fname)
        self._shape = self._df.shape

    def cleaning_data(self, col_names):
        self._df = self._df[col_names]
        return self._df

    def rename_col(self, new_col):
        """
        Takes in a list of new column names,
        return a dataframe
        """
        column_dict = dict(zip(list(self._df.columns), new_col))
        self._df = self._df.rename(columns=column_dict)
        return self._df

    def filter_data(self, col, col_min, col_max):
        """
        Takes in a column in interest, the min and max values of the column,
        We assume the survey skip the whole section,
        so we only need to filter by one column.
        Return a filtered dataset.
        """
        filtered_d = self._df[(self._df[col] >= col_min) &
                              (self._df[col] <= col_max)]
        return filtered_d

    def fill_nas(self, values):
        """
        Takes in a list of values that we view as NaNs (e.g. -9) and a data
        return a filled na data
        """
        for col in self._df.columns:
            self._df.loc[self._df[col].isin(values), col] = np.nan
        return self._df

    def gender_response(self):
        """
        Add gender response to the dataset in order to make further computation
        """
        self._df['gender'] = self._df.apply(lambda row:
                                            gender_label(row), axis=1)
        return self._df

