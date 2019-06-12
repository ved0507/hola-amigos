print("Numpy starts here")

import numpy as np



arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(type(arr))
print("Dimension",arr.ndim)
print("shape",arr.shape)
print("size & type",arr.size,arr.dtype)

#transpose of array
print("Before transpose \n",arr)
print("============")
print("Transpose\n",arr.T)

#unary operators
#min max sum 
print(arr.min(axis=1))
print(arr.max(axis=1))
print("Sum",sum(arr))

print(np.arange(1,10).reshape(3,3))


list2=[]
if len(list2) == 0:
	print("empty")
else:
	print("not")
#find unique from list
arr1=[1,2,3,3,3,3,4,5,6,7,7,8,9]
arr2=[]

for i in arr1:
		if i in arr2:
			continue
		else:
			arr2.append(i)
print(arr2)

#multiply all numbers in list



import random
arr3=[]
for i in range(5):
	x=random.randint(1,10)
	if x not in arr3:
		arr3.append(x)
print(arr3)
j=1
def mult(r):
	j=1
	for i in arr3:
		j=j*3
	return j

print(mult(arr3))

		
	
list3=[1,2,3]
print(np.prod(list3))

from functools import *
n=reduce(lambda x,y:x*y,list3)