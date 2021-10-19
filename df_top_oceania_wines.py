import pandas as pd

wines = pd.read_csv('/home/studio/Downloads/winemag-data-130k-v2.csv')

df = pd.DataFrame(wines)
nation = [ 'Australia','New Zealand']

oceania = df[(df['points'] > 95) & df['country'].isin(nation)]
print(oceania.head(100))


# print(autraliaWines[0:95])
# print(nzWines[0:95])
