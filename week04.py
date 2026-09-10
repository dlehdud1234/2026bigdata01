import pandas as pd
scores = [100, 60, 30, 10]
average =  pd.Series(scores).mean()
print(average)

