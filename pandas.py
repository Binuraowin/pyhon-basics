import pandas as pd

url="https://raw.githubusercontent.com/COVID19-Malta/COVID19-Data/master/COVID-19%20Malta%20-%20Aggregate%20Data%20Set.csv"
pf = pd.read_csv(url)
pf.head(10)