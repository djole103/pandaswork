import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel', 'Steven', 'Isaac', 'Tommy']
random.seed(500)
random_names = [names[random.randint(low = 0, high = len(names))] for i in range(1000)]
print(random_names[:10])

births = [random.randint(low = 1, high = 1000) for i  in range(1000)]
babies = list(zip(random_names, births))

df = pd.DataFrame(data = babies, columns = ['Name', 'Births'])
print( df[:10])

path = '../data/babybirths.txt'
df.to_csv(path ,index = False, header = False)
df = pd.read_csv(path)
print(df.head())
#problem: treats the first record as the headers
df = pd.read_csv(path, names = ['Name' , 'Births'])
print(df.head())
print(df['Name'].describe())
#still have multiple entries for a single name, reduce to 8 unique entries
name = df.groupby('Name')
df = name.sum()
print(df)

df.sort(['Births'], ascending = False)
df['Births'].plot(kind = 'bar')
print(df.sort(columns = 'Births', ascending = False))
plt.show()

