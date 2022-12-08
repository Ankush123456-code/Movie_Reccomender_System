import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def histogram(data, column_name, bins):
    plt.figure(figsize=(20, 10))
    plt.hist(data[column_name], bins=bins)
    plt.show()


def jointplot(data, x: str, y: str):
    sns.jointplot(x=x, y=y, data=data)
    plt.show()
