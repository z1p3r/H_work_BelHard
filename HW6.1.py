import pandas as pd
dt={'Name' : [input("Name")], 'Surname' : [input("SurName")], 'Age':[input("Age")]}
df=pd.DataFrame(dt,columns=dt.keys())
df.to_csv('HW6.1.csv', index=False)