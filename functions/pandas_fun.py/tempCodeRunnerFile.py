sales = pd.merge(orders_df, customers_df, on="customer_id", how="inner")
print("Inner Join (only matching customer_id):")    
print(sales)

sales = pd.merge(orders_df, customers_df, on="customer_id", how="outer")
print("\nOuter Join (all records, NaN for non-matching):")
print(sales)

sales = pd.merge(orders_df, customers_df, on="customer_id", how="left")
print("\nLeft Join (all orders, NaN for non-matching customers):")
print(sales)