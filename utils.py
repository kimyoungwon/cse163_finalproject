# Utilities that we might use in other files
# but not that directly connected to the FF_wave()
import numpy as np
import math


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
    Returns 1 for father, 0 for mother, nan for no response available
    """
    if np.isnan(row['m_agg_1']) & np.isnan(row['f_agg_1']):
        return np.nan
    elif np.isnan(row['f_agg_1']):
        return 0
    else:
        return 1


def check_approx_equals(expected, received):
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    try:
        if type(expected) == dict:
            # first check that keys match, then check that the
            # values approximately match
            return expected.keys() == received.keys() and \
                all([check_approx_equals(expected[k], received[k])
                    for k in expected.keys()])
        elif type(expected) == list or type(expected) == set:
            # Checks both lists/sets contain the same values
            return len(expected) == len(received) and \
                all([check_approx_equals(v1, v2)
                    for v1, v2 in zip(expected, received)])
        elif type(expected) == float:
            return math.isclose(expected, received, abs_tol=0.001)
        else:
            return expected == received
    except Exception as e:
        print(f'EXCEPTION: Raised when checking check_approx_equals {e}')
        return False


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    assert check_approx_equals(expected, received), \
        f'Failed: Expected {expected}, but received {received}'
