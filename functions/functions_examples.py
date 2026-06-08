# Temp Conversion Function
# def temp_convert():
#     user_input=input("Whether you need to Celsius or Fahrenheit:", ).title()
#     if user_input=="Celsius":
#         Temp=float(input("Enter temperature in Celsius:"))
#         Fahrenheit=(((9/5)*Temp)+32)
#         print(f"{Fahrenheit}F")

#     elif user_input=="Fahrenheit":
#         Temp=float(input("Enter temperature in Fahrenheit:"))
#         Celsius = ((Temp-32)*5/9)
#         print(f"{Celsius} C")


# temp_convert()

# Password strength check
# password = input("enter your password:")
# def check_password(password):
#     special_characters = any(("@","%","&","*") in password)
#     lower = any(char.islower() for char in password)
#     upper = any(char.isupper() for 

# Cost of shopping list
# def total_cost():
    # for values in cart.items():

cart = {}
while True:
    items= (input("Enter items with their cost:"))
    if items=="":
        break
cart.update(items)
print("Your shopping list is as follows:",cart)
name,cost=items.split(":")

def total_cost(cart):
    Total=0
    for cost in cart.values():
        Total+=cost
        print(Total)
 
 

