# %%

import pandas as pd

df = pd.read_csv('rides.csv')
df

# %%
mask = df.eval('name.isnull() | distance <= 0')
mask

# %%
df2 = df[~mask]
df2

# %%
df
# %%
