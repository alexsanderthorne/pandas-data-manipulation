import pandas as pd
import numpy as np

x = pd.DataFrame({'x':[1,2,3], 'y':[3,4,5]})
print(x)

x.iloc[1] = {'x':8, 'y':231}
print(x)
