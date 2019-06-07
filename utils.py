# Utilities that we might use in other files
# but not that directly connected to the FF_wave()
import numpy as np


def make_colnames(string, n, gender=None):
    """
    Takes in gender, string(column header), the length of colnames
    Gender can only be "m" or "f"
    Return a list of column names
    Making iterations faster
    """

    col_list = []
    for i in range(1, n+1):  # we want col index to start from 1
        if gender is None:
            s = string+'_'
        else:
            s = gender+'_'+string+'_'
        s += str(i)
        col_list.append(s)
    return col_list


def gender_label(row):
    """
    Takes in a row from dataframe, and check mother's or father's response
    Returns 1 for father, 0 for mother
    """
    if np.isnan(row['m_agg_1']):
        return 1
    else:
        return 0 