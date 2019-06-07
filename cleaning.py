# This class constructs a class from the FF_allwaves file

from utils import make_colnames, gender_label
import pandas as pd
import numpy as np


class FF_wave:
    """
    This FF_wave class represent a dataframe with several methods
    related to etracting data and manipulating the data for further usage
    """
    def __init__(self, fname, col_names):
        """
        Initialize a new FF_wave object. fname is a string of path/file name
        and the col_names is a list of column that we want to read in from
        the csv (FF_wave) file
        """
        self._fname = fname
        # Read in the data using the order of our col_names
        self._df = pd.read_csv(fname, usecols=col_names)[col_names]
        self._shape = self._df.shape

    def rename_col(self, new_col):
        """
        Takes in a list of new column names,
        Returns a renamed header dataframe
        """
        column_dict = dict(zip(list(self._df.columns), new_col))
        self._df = self._df.rename(columns=column_dict)
        return self._df

    def fill_nas(self, values):
        """
        Takes in a list of values that we view as NaNs (e.g. -9) and a data
        Returns a filled na data
        """
        for col in self._df.columns:
            self._df.loc[self._df[col].isin(values), col] = np.nan
        return self._df

    def replacement(self, col, to_replace, value):
        """
        Takes in a list of column names where you want to replace the values,
        an int/float to be replaced, and an int/float to replace with
        Return a dataframe
        """
        self._df[col] = self._df[col].replace(to_replace, value)
        return self._df

    def gender_response(self):
        """
        Add gender response to the dataset in order to make further computation
        Return a dataframe
        """
        self._df['gender'] = self._df.apply(lambda row:
                                            gender_label(row), axis=1)
        return self._df

    def avg_subscale(self, gender, category, num_col):
        """
        Takes i either "del" or "agg" for category, "m" or "f" for gender,
        and the number of columns that needs to be sum up
        Returns a dataframe withe new column
        """
        col_list = make_colnames(category, num_col, gender)
        new_col = gender + '_' + category + '_avg'
        self._df[new_col] = self._df[col_list].mean(axis=1, skipna=True)
        return self._df

    def sum_subscale(self, category, num_col):
        """
        Takes i either "del" or "agg" for category, and the number of columns
        that needs to be sum up
        Returns a dataframe withe new column
        """
        col_list = make_colnames(category, num_col)
        new_col = category + '_sum'
        self._df[new_col] = self._df[col_list].sum(axis=1, skipna=False)
        return self._df

