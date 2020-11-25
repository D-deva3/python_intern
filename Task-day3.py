# Task3
# 1
x = {" Devadharshini": 10, " vasanthi": 10, " dhanya ": 10}
y = {"Devadharshini": 10, "vasanthi": 10}
z = x.copy()
for key, value in y.items():
    z[key] = value
print(z)
# 2
y.pop("Devadharshini")  # Removes the specified key
x.popitem()  # Removes the last inserted item
print(x)
print(y)
# 3
Laptop = {"asus", "lenova"}
Colour = {" silver", "black"}
new_dic = dict(zip(Laptop, Colour))
print(new_dic)
# 4
a={"cookie" ,"popcorn" ,"noodles"}
print(len(a))
# 5
b={"popcorn"}
print(a-b)
