import pandas as pd
orders = {
    "order_id": [1, 2, 3, 4, 5],
    "customer_id": [101, 102, 103, 104, 105],
    "amount": [250, 150, 300, 200, 350]
}
customers = {
    "customer_id": [101, 102, 103, 106, 107],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
orders_df = pd.DataFrame(orders)
customers_df = pd.DataFrame(customers)

# sales = pd.merge(orders_df, customers_df, on="customer_id", how="inner")
# print("Inner Join (only matching customer_id):")    
# print(sales)

# sales = pd.merge(orders_df, customers_df, on="customer_id", how="outer")
# print("\nOuter Join (all records, NaN for non-matching):")
# print(sales)

# sales = pd.merge(orders_df, customers_df, on="customer_id", how="left")
# print("\nLeft Join (all orders, NaN for non-matching customers):")
# print(sales)

# sales = pd.merge(orders_df, customers_df, on="customer_id", how="right")
# print("\nRight Join (all customers, NaN for non-matching orders):")
# print(sales)