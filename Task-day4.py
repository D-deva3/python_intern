#1) write a program to create a list of n integer values and do the following
 L1=['1','2','3','4','5']

 # a) add an item in to the list (using function)
 L1.append('6')
print(L1)

 # b) delete(using function)
L1.remove('2')
print(L1)

 # c) store the largest number frrpm the list to a variable
 print(max(L1))

 # d) store the smallest number from the list to a variable
 print(min(L1))

 #2 )create a tuple and point the reverse of the created tuple
 tuple = ('1','2','3','good','6.23')
 reversedtuples = tuple[::-1]
 print(reversedtuples)

 #3 )create a tuple and convert tuple into list
tuple = ('25','35','45','7.45','good')
 list = list(tuple)
 print(type(list))
<class 'list'>
print(list)
