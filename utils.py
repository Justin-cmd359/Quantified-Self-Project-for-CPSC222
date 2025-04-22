"""
Justin Yi
4/21/25
CPSC 222
Description:
This file contains utility functions used for
my Quantified Self Project
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_from_file(infile):
    df = pd.read_csv(infile)
    return df
def drop_column(df, column):
    df.drop(column, axis=column)
    return df