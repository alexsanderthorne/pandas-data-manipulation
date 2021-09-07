import pandas as pd
import numpy as np

wines = pd.read_csv(
    '/home/studio/Downloads/winemag-data-130k-v2.csv')
#desc = wines['points']

country = wines['country']
df = pd.DataFrame(wines)
nation = ['Italy']
italyWines = df.loc[df['country'].isin(nation)]

print(italyWines['points'])
