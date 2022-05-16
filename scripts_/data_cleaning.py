import pandas as pd
import numpy as np


class DataCleaning:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def percent_missing(self, df: pd.DataFrame):

        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

    # Count number of missing values per column
        missingCount = df.isnull().sum()

    # Calculate total number of missing values
        totalMissing = missingCount.sum()

    # Calculate percentage of missing values
        print("The Telecom dataset contains", round(
            ((totalMissing/totalCells) * 100), 2), "%", "missing values.")

        return df
