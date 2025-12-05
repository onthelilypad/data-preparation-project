import pandas as pd
df = pd.read_csv("iris.csv")
print(df.head())

df = df.dropna()

df.columns = [col.strip().lower().replace(' ', '-') for col in df.columns]

print("\nData after Cleaning:")
print(df.head())