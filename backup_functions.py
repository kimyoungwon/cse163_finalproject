
import pandas as pd

def clean_data(data, col_list):
    new_df = data[col_list]
    return new_df


def rename(data, new_col):
    """
    Takes in a list of new column names,
    return a dataframe
    """
    column_dict = dict(zip(list(data.columns), new_col))
    res = data.rename(columns=column_dict)
    return res


def filter_data(data, col, col_min, col_max):
    """
        Takes in a column in interest, the min and max values of the column,
        We assume the survey skip the whole section,
        so we only need to filter by one column.
        Return a filtered dataset.
    """
    filtered_d = data[(data[col] >= col_min) & (data[col] <= col_max)]
    return filtered_d


def fill_nas(data, values):
    """
    Takes in a list of values that we view as NaNs (e.g. -9) and a data
    return a filled na data
    """
    for col in data.columns:
        data.loc[data[col].isin(values), col] = np.nan
    return data

def gender_response(data):
    """
    Add gender response to the dataset in order to make further computation
    """
    return data['gender'] = data.apply(lambda row: label(row), axis=1)


def avg_subscale(data, gender, category, num_col):
    # category can only be "del" or "agg"
    # gender can only be "m"/"f"
    col_list = make_colnames(gender, category, num_col)
    new_col = gender + '_' + category + '_sum' 
    data[new_col] = data[col_list].mean(axis=1, skipna=True)
    return data

def replacement(data, col, to_replace, value):
    data[col] = data[col].replace(to_replace, value)
    return data