import pandas as pd
from pandas.api.types import is_numeric_dtype

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
dtypes = diamonds.dtypes
columns = dtypes[dtypes.apply(is_numeric_dtype)].index
display(diamonds[columns])