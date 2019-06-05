import scipy.stats as sp
import seaborn as sns
import matplotlib.pyplot as plt

def get_pearsonr(dataframe, names_of_variables):
    num = 0
    for variable1 in names_of_variables:
        num += 1
        for variable2 in names_of_variables[num:]:
            if variable1 != variable2:
                correlation = sp.pearsonr(dataframe[variable1], dataframe[variable2])
                print("The significance (p) of correlation " + "(" + str(correlation[0]) + ")" + " between " + variable1 + " and " + variable2 + ": " + str(correlation[1]))


def plot_correlations(dataframe, names_of_variables):
    '''
    '''
    df = sns.dataframe[names_of_variables]
    sns.pairplot(df, kind="scatter", hue="species", markers=["o", "s", "D"], palette="Set2")
    plt.show()


def mean_std_of_variables(dataframe, names_of_variable):
    '''
    '''
    return dataframe[names_of_variable].describe()['mean':'std']
