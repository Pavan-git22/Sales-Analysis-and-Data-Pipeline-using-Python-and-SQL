dict = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25,
    6:36,
    7:49,
    8:64,
    9:81,
    10:100,
    "name":"a",

}
print(dict)
print("The square of 5 is:",dict[5])
dict.update({11:121})
# del dict[1]
dict.pop(1)
print(dict)
for key,values in dict.items():
    print(f"{key}:{values}")