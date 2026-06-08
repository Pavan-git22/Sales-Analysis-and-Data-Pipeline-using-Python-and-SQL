# Even or odd function
def even_or_odd(num):
    # num=int(input("Enter a number:"))
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
even_or_odd(24)
# print(Result)


# Add function
def add(a,b):
    return a+b
# Calls add function and store it as result variable
result = add(2,4)
print(result)

# Default parameters

def greet(name="pavan"):
    print(f"Hello {name} ")

greet()

# Positional arguments
def argument(*args):
    #Creates a tuple
    print(args)
    for num in args:
        print(num)
argument(1,2,3,4,5,6)

#Keyword arguments
def key_argument(**kwargs):
    # Creates a dictionary
    for key,values in kwargs.items():
        print(f"{key}:{values}")
key_argument(Name="Krish",age=32)

# Positional and Keyword arguments
def arguments(*args,**kwargs):
    for num in args:
        print(num)
    for key,values in kwargs.items():
        print(f"{key}:{values}")
#Imp: Always positional arguments should be first then followed by key arguments
arguments(1,2,3,4,5,6,Name="Krish",age=32)
