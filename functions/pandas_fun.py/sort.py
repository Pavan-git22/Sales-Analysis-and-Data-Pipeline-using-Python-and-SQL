import pandas as pd
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 40, 45],
    "salary": [50000, 60000, 70000, 80000, 90000],
    "performance": [4.5, 4.0, 3.5, 4.8, 4.2],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df_sorted = df.sort_values(by=["age","salary"], ascending=False ,inplace=True)
print("\nDataFrame sorted by age and salary in descending order:")
print(df)