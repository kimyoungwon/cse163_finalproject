#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from cleaning import FF_wave
from utils import make_colnames

################################################################################
# Step 1: Read and clean .......data set.
################################################################################
"""
def read_csv(path):
    '''
    Reads the CSV file at path, and returns a dataframe.
    '''
    return 

def means_of_variables(dt, name_of_variable):
    return

def get_pearsonr(dt,names_of_variables):
    return

def bar_grapgh(dt, variable):
    return

def scatter_plot(dt, variable1, variable2):
    return
"""
################################################################################
# Step 3: Machine Learning Model
################################################################################

def fit_and_predict_gender(data, gender, response_var):
    """
    Takes in a data as parameter, gender(1/0) and a string of response variable
    Train a linear regression model with training set, and prints out
    coefficients.
    Returns the float of test mean square error.
    """
    filter_df = data[data['gender'] == gender]
    if gender == 0:
        filter_df = data[['m_agg_avg', response_var]]
    else:
        filter_df = data[['f_agg_avg', response_var]]
    filter_df = filter_df.dropna()
    X = filter_df.loc[:, filter_df.columns != response_var]
    Y = filter_df[response_var]
    (X_training, X_testing,
     Y_training, Y_testing) = train_test_split(X, Y, test_size=0.2,
                                               random_state=1)
    model = LinearRegression()
    model.fit(X_training, Y_training)
    print("The learned coefficient is: ", list(zip(X, model.coef_)))
    rmse = np.sqrt(mean_squared_error(Y_testing, model.predict(X_testing)))
    print("The RMSE of test data is ", rmse)
    return rmse


################################################################################
# Main Function
################################################################################

def main():
    interest_col = ['m5k2a', 'm5k2b', 'm5k2c', 'm5k2d', 'f5k2a', 'f5k2b',
                    'f5k2c', 'f5k2d', 'k5f1a', 'k5f1b', 'k5f1c', 'k5f1d', 
                    'k5f1e', 'k5f1f', 'k5f1g', 'k5f1h', 'k5f1i', 'k5f1j',
                    'k5f1k', 'k5f1l', 'k5f1m', 'k5f1n', 'k5f1o', 'k5f1p',
                    'k5f1q', 'ch5ppvtss']
    data = FF_wave('FF_allwaves_2019.csv', interest_col)
    new_colnames = make_colnames('agg', 4, 'm') + make_colnames('agg', 4, 'f')\
        + make_colnames('del', 17)+['ppvt_ss']
    data.rename_col(new_colnames)
    data.fill_nas([-6, -3, -9, -5, -1, -2])
    data.replacement(make_colnames('del', 17), 2, 0)
    data.gender_response()
    data.avg_subscale('m', 'agg', 4)
    data.avg_subscale('f', 'agg', 4)
    filtered_df = data.sum_subscale('del', 17)
    # 4 regressions of machine learning with different gender/response variable
    fit_and_predict_gender(filtered_df, 1, 'ppvt_ss')
    fit_and_predict_gender(filtered_df, 0, 'ppvt_ss')
    fit_and_predict_gender(filtered_df, 1, 'del_sum')
    fit_and_predict_gender(filtered_df, 0, 'del_sum')

if __name__ == "__main__":
    main()