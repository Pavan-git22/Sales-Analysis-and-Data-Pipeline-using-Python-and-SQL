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

new_df = df["name"]
print(new_df)

sub_df = df[["name", "age"]]
print(sub_df)


# df = pd.read_excel("C:\\Users\\pavan\\OneDrive\\Desktop\\VS Code\\python\\functions\\SampleSuperstore.xlsx")
# print(df.info())