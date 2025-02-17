# %%
import pandas as pd

df = pd.read_csv('rides.csv')
df
# %%
# Find out all the rows that have bad values
# - Missing values are not allowed
# - A plate must be a combination of at least 3 upper case letters or digits
# - Distance much be bigger than 0
# %%
df2 = df.isnull().any(axis=1)
df2
# %%
df3 = df['distance'] > 0
df3
# %%
