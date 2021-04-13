import pandas as pd
import os


def load_data():
    this_directory = os.path.dirname(os.path.abspath(__file__))
    data = pd.read_csv(os.path.join(this_directory, 'HN_radiomicFeatures.csv'), index_col=0)

    return data
