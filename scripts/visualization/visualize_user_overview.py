import matplotlib.pyplot as plt

def plot_duration_histogram(metrics, bins=30):
 
    plt.hist(metrics['Duration'], bins=bins)
    plt.xlabel('Duration')
    plt.ylabel('Frequency')
    plt.title('Histogram of Call Durations')
    plt.show()


def plot_variable_histograms(dataframe):

    variables = ['Total_DL', 'Total_UL', 'SM_DL', 'SM_UL', 'Google_DL', 'Google_UL', 'Email_DL', 'Email_UL',
                 'YouTube_DL', 'YouTube_UL', 'Netflix_DL', 'Netflix_UL', 'Gaming_DL', 'Gaming_UL', 'Other_DL', 'Other_UL']

    for variable in variables:
        plt.hist(dataframe[variable], bins=30)
        plt.xlabel(variable)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {variable}')
        plt.show()
 