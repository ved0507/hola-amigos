#----Loops-----
#for loops
arr=["bannana","apple","pineapple","grapes"]

for i in arr:
	print (i)
	

arr1=[12,13,15]
total=0
for i in arr1:
	total=total+i
	print(total,"-->",end=" ")	
print("\n")



#Sum of all multiples of three and five that are less than 100
import random
ranarr1=[]
def mul35(arr1):
	for i in arr1:
		if i%3 == 0 and i%5 == 0:
			print("Multiples of 3 and 5==>",i)
for i in range(100):
	ranarr1.append(i)
mul35(ranarr1)
print("\n")
print("WHILE LOOPS STARTS FROM HERE==>\n")
#============While loop
#loop with else block
w=0
while w<10:
	print(w,end=" ")
	w+=1
else:
	print("while loop else block ends here==>\n")
wlist=[1,2,3,4,566,77,8,11]
for i in range(len(wlist)):
	print(i,end=" ")
else:
	print("for loop else block ends here")
	
	
#Nested loop

for i  in range(5):
	print("*",end=" ")
	for j in range(2*i):
		print("*",end=" ")
	print(end="\n")
# *
# * *
# * * * *
# * * * * * *
# * * * * * * * *
	
		
	
		