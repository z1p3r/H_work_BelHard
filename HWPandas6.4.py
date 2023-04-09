import pandas as pd
df = pd.read_csv("6.csv")
a = df['Absolute magnitude(Mv)'].var()
print(df['Spectral Class'].value_counts())
print(a)