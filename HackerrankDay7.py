# print("Hacker rank questions")

# n=int(input())
# arr1=[]

# for  i in range(n):
	# arr=list(map(int, input().rstrip().split()))
	# arr1.extend(arr)

# print(arr1)


# print(" ".join(map(str,arr1[::-1])))


#n - names - keys
#Phone mubers - values

# dict={}
# for i in range(2):
	# val=input()
	# dict[val]=int(input())
# print(dict)

# if "ved" in dict:
	# print("")
	

x=[i for i in range(4) if i%2==0]
print(x)

#x, y, z, n = int(input()), int(input()), int(input()), int(input())
#print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

#n = int(input())
arr = [6,3,44,5,33]
first=arr[0]
sec=0
for i in range(1,len(arr)):
	print(arr[i])
	
	if arr[i] > sec:
		#print(first,arr[i])
		sec=first
		first=arr[i]
print(sec,first)
		
	
