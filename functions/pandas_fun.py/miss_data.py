import pandas as pd
data = {
    "name": ["Alice", None, "Charlie", "David", "Eve"],
    "age": [25, None, 35, 40, 45],
    "salary": [50000, None, 70000, 80000, 90000],
    "performance": [4.5, 4.0, None, 4.8, 4.2],
    "city": ["New York", "Los Angeles", "Chicago", "mandya","Phoenix"]
}
df = pd.DataFrame(data)
print(df)
# df.dropna(inplace=True)
# print("\nDataFrame after dropping rows with missing values:")
# print(df)

# df.fillna("0", inplace=True)
# print("\nDataFrame after filling missing values with 0:")
# print(df)

df["age"].fillna(df["age"].mean(), inplace=True)
print("\nDataFrame after filling missing age values with mean:")
print(df)