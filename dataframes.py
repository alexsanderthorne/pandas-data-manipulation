import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': list('ABBC'), 'col2': list('ZZXY')})

print(df)
df['color'] = np.where(df['col2'] == 'Z', 'green', 'red')

print(df)
