import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datacamp/courses-introduction-to-python/master/datasets/baseball.csv")
description = df.describe()

print(df.head(20))
print(description)
