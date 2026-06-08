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


high_salary = df[df["salary"] > 60000]
print("Employees with salary greater than 60000:")  
print(high_salary)

print("\n")

highest_performance = df[(df["performance"] > 4.0) & (df["age"] < 40)]
print("Employees with performance greater than 4.0 and age less than 40:")
print(highest_performance)

print("\n")

highest_performance = df[(df["performance"] > 4.0) | (df["age"] < 40)]
print("Employees with performance greater than 4.0 or age less than 40:")
print(highest_performance)


