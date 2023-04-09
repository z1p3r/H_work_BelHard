import pandas as pd
df = pd.read_csv("6.csv")
print(df)
df["Tmean"] = df['Temperature (K)'].mean()
df["Tmax"] = df['Temperature (K)'].max()
df["Tmin"] = df['Temperature (K)'].min()
df["Delta_T"] = abs(df["Temperature (K)"] - df["Tmean"])
print(df)
df["T1"] = (df["Tmax"]/2)
print(df.T1)
df[(df["Delta_T"] >= 20000) & (df["Temperature (K)"] > 1939)]
print(df)