import pandas as pd
import pandas as pd
import numpy as np

dates = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.random.randn(8, 4), index=dates,
                  columns=['A', 'B', 'C', 'D'])

#s = df['A']
# s[dates[5]]

df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()

print(df)
# print(s)
