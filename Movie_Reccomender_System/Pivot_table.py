import pandas as pd


def pivot_table(data, index, column, value):
    try:
        data = pd.pivot_table(data=data, index=index,
                              columns=column, values=value)
        return data
    except:
        return "not exeuted"
