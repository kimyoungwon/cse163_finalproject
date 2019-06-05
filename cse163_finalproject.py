#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

from cleaning.py import FF_wave
from utils import make_colnames, gender_label

################################################################################
# Step 1: Read and clean .......data set.
################################################################################

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

if __name__ == "__main__":
    main()