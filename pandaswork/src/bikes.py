import pandas as pd
import matplotlib.pyplot as plt
broken_df = pd.read_csv('../data/2012cyclistdata.csv')
print(broken_df[:3])
df = pd.read_csv('../data/2012cyclistdata.csv', sep=',' , encoding = 'latin1', parse_dates = ['Date'], dayfirst=True, index_col = 'Date')
print(df[:3])

print(df['Berri 1'])

df.plot()
plt.show()

