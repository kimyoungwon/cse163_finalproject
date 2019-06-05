# Utilities that we might use in other files
import numpy as np


def make_colnames(gender, string, n):
    # Takes in gender, string(column header), the length of colnames
    # Gender can only be "m" or "f"
    # Return a list of column names
    # Making iterations faster
    col_list = []
    for i in range(1, n+1):  # cuz we want values starting from 1
        s = gender+'_'+string+'_'
        s += str(i)
        col_list.append(s)
    return col_list


def gender_label(row):
    """
    Check whether it's mother's response or father's
    1: father
    0: mother
    """
    if np.isnan(row['m_agg_1']):
        return 1
    else:
        return 0 