print("# Python Scripts here #")

#Add two numbers

num1=4.5
num2=6.7
print("\n")
print("\n")
sum1=num1+num2
print('Sum of {0} and {1} is {2} '.format(num1,num2,sum1) )
sum2=0
#Find the sum of range 10 

for i in range(10):
	if(i%2==0):
		print("num",i)	
		sum2=sum2+i 
print("Sum of all values ", sum2)


#find the largest of all three numbers

#12 35 89
list1=[12,35,89]
if(list1[0] > list1[1]):
	print("{} is largest of all three".format(list1[0]))
if(list1[2] > list1[0]):
	print("{} is largest of all three".format(list1[2]))

	
	
#LCM of two numbers

x=34
y=89
if(x>y):
	greater = x
else:
	greater = y

while(true):
	lcm = greater
	
	
	

