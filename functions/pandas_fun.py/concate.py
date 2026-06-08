import pandas as pd
region1 = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "sales": [100, 150, 200]
})
region2 = pd.DataFrame({
    "name": ["David", "Eve", "Frank"],
    "sales": [250, 300, 350]
})  
# Concatenate along rows (default)
concatenated_rows = pd.concat([region1, region2], ignore_index=True)
print("Concatenated along rows:")
print(concatenated_rows)
print("\n")
# Concatenate along columns
concatenated_cols = pd.concat([region1, region2], axis=1)
print("Concatenated along columns:")
print(concatenated_cols)