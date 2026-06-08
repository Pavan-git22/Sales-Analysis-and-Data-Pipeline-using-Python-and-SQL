import pandas as pd
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 40, 45],
    "salary": [50000, 60000, 70000, 80000, 90000],
    "performance": [4.5, 4.0, 3.5, 4.8, 4.2],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
df = pd.DataFrame(data)
print("DataFrame created from dictionary:")
print(df)

df["bonus"] = df["salary"] * 0.1
print("\nDataFrame after adding bonus column:")
print(df)

df.insert(2, "department", ["HR", "Finance", "IT", "Marketing", "Sales"])
print("\nDataFrame after inserting department column:")
print(df)

df.loc[0, "age"] = 26
print("\nDataFrame after updating Alice's age:")
print(df)

df['salary'] = df['salary'] * 1.05
print("\nDataFrame after giving a 5% raise to all employees:")
print(df)

df.drop("performance", axis=1, inplace=True)
print("\nDataFrame after dropping performance column:")
print(df) 