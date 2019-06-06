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

# This has to seperate father/mother per call
def fit_and_predict_ppvt_gender(data, gender):
    """
    Takes in a data as parameter, gender(1/0)
    Train the model and of 
    Returns the float of test mean square error.
    """
    filter_df = data[data['gender']==gender]
    if gender == 0:
        filter_df = data[['m_agg_avg','ppvt_ss']]
    else: 
        filter_df = data[['f_agg_avg','ppvt_ss']]
    filter_df = filter_df.dropna()
    X = filter_df.loc[:, filter_df.columns != 'ppvt_ss']
    Y = filter_df['ppvt_ss']
    (X_training, X_testing,
     Y_training, Y_testing) = train_test_split(X, Y, test_size=0.2, random_state=1)
    model = LinearRegression()
    model.fit(X_training, Y_training)
    return mean_squared_error(Y_testing, model.predict(X_testing))

# This kinda put them in the same model, but when doing regression, 
# I still need to pull out only father/mother (cuz the values will be nan)
# but this consider gender as regressor?
def fit_and_predict_ppvt(data):
    filter_df = filter_df.dropna(subset=['ppvt_ss', 'f_agg_avg'])
    X = filter_df.loc[:, filter_df.columns != 'ppvt_ss']
    X = pd.get_dummies(X, columns=['gender'])  # consider gender as a regressor
    Y = filter_df['ppvt_ss']
    X_2 = X[['f_agg_avg', 'gender_0', 'gender_1']]
    (X_training, X_testing,
        Y_training, Y_testing) = train_test_split(X_2, Y, test_size=0.2, random_state = 1)
    model = LinearRegression()
    model.fit(X_training, Y_training)
    return mean_squared_error(Y_testing, model.predict(X_testing))

################################################################################
# Main Function
################################################################################

def main():
    data = FF_wave('FF_allwaves_2019.csv')
    interest_col = ['m5k2a', 'm5k2b', 'm5k2c', 'm5k2d', 'f5k2a', 'f5k2b',
                    'f5k2c', 'f5k2d', 'ch5ppvtss']
    new_colnames = make_colnames('m', 'agg', 4) + make_colnames('f', 'agg', 4)+ ['ppvt_ss']
    data.cleaning_data(interest_col)
    data.rename_col(new_colnames)
    data.fill_nas([-6, -3, -9, -5, -1, -2])
    data.gender_response()
    data.avg_subscale('m', 'agg', 4)
    filtered_df = data.avg_subscale('f', 'agg', 4)
    #print(filtered_df.head())

if __name__ == "__main__":
    main()