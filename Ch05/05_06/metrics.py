# %%
import pandas as pd

df = pd.read_csv('metrics.csv', parse_dates=['time'])
df
# %%

df2 = pd.melt(
    df,
    value_vars=['cpu', 'memory'],
    id_vars=['time'],
    var_name='metric',
)
df2

# %%
