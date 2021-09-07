import pandas as pd

wines = pd.read_csv('/home/studio/Downloads/winemag-data-130k-v2.csv')

country = wines['country']
df = pd.DataFrame(wines)
nation = ['Australia']
nation2 = ['New Zealand']

autraliaWines = df.loc[df['country'].isin(
    nation)]

nzWines = df.loc[df['country'].isin(
    nation2)]

# print(autraliaWines)
print(nzWines)
