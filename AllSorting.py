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
