#1)Create a module and import it
import mymodule as md
print(md.list1)
for i in range(len(md.list1)):
   md.list1[i]=i+3
print(md.list1)

#2)Import pandas and use it
import pandas as pd
a=["deva","roja","dora"]
b=[14,24,21]
c=list(zip(a,b))
df=pd.DataFrame(data=c,columns=['Name','Age'])
print(df)

#3)Generate random number
import random as rd
print("Random Number:",rd.randint(1,100))

#4)Import sys package
import sys
print("\n".join(sys.path))

#5) pip install numpy  #install a package using pip
#  pip uninstall numpy #uninstall a package using pip
