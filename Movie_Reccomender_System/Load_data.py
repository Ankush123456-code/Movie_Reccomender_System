
import pandas as pd


def load_data(data, sep=None, column_name=None):
    try:
        dataset = pd.read_csv(data, sep=sep, names=column_name)
        return dataset
    except:
        return "Failed"
