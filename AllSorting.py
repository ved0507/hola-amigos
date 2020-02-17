print("-------Bubble sorting-------")
lst=[]
lst1=[]
import random

for i in range(10):
	lst.append(random.randint(1,200))
	lst1.append(random.randint(1,300))
print("Before sorting")
print(lst)
def bubble(lst):
	length=len(lst)-1
	isSorted=False
	while not isSorted:
		isSorted=True
		for i in range(length):
			if lst[i] > lst[i+1]:
				isSorted=False
				lst[i] , lst[i+1] =lst[i+1] , lst[i]
	print("After sorting")
	return lst
print(bubble(lst))
print("============================================$=============")
print("Selection sort starts here")
print("Before sorting")
print(lst1)

def selection(lst1):
	
	for i in range(len(lst1)-1):
		minimumval=lst1.index(min(lst1[i:]))
		lst1[i] , lst1[minimumval] =lst1[minimumval] , lst1[i]
	
	return lst1
print(selection(lst1))



#selection sort

A=[65,11,25,12,5]

for i in range(len(A)):
    min_index=i
    for j in range(i+1,len(A)):
        if A[min_index] > A[j]:
	          min_index = j
    A[i],A[min_index] = A[min_index],A[i]
print('sorted array')

for i in range(len(A)):
    print(A[i],end=' ')


###Quick Sorting -Divide and rule  algorithm

#avarage  complexity O(nlogn)
''' Divide and conquer 
inplace
unstable'''

def Partition(arr,low,high)	:
	i=(low - 1)
	piv = arr[high]
	for j in range(low,high):
		if arr[j]<piv:
			i=i+1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
def quicksort(arr,low,high)
  if low<high:
	pi = partition(arr,low,high)
	quicksort(arr, low, pi-1)
	quicksort(arr,pi+1,high)
arr=[11,33,44,66,10,23]
n=len(arr)
quicksort(arr,0,n-1)
for i in range(n):
	print(arr[i])
