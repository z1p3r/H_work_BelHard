import pandas as pd
df = pd.read_csv("6.csv")
a = df['Absolute magnitude(Mv)'].mean()
print("Среднее:", a)
print(df['Star color'].value_counts())