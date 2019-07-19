import array
import numpy as np
i=0
arr=array.array('i',[1,2,3,4,5,6])
print(arr)
for i in arr:
	print(i,end=" ")
print(end="\n")
print(arr.pop(2))

#extend
arr1.extend(arr2) 



#==Numpy numeric python is for computation on homogenous n dim
#multiply
list1=[5,3,7,1,2,9,23]
list2=list1[::-1]
a1=np.array(list1)
a2=np.array(list2)
print(a1*a2)

# a[start:stop:step] 

a2=np.arange(200,1,-1)
print(a2[a2>100])




