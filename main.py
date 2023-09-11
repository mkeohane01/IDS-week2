import pandas as pd
import matplotlib.pyplot as plt


# read and describe data
df = pd.read_csv("https://raw.githubusercontent.com/datacamp/courses-introduction-to-python/master/datasets/baseball.csv")
description = df.describe()
print(df.head(10))
print(description)

position_counts = df['Position'].value_counts()

# visualize and plot data
plt.figure(figsize=(10, 6))
position_counts.plot(kind='bar')
plt.title('Histogram of Players by Position')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.xticks(rotation=45)  
plt.tight_layout()
plt.savefig('position_histogram.png')
plt.show()
