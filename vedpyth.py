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

	
	#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))


#lambdas  - anaonymus  - map - filters
 
 #generators  are type of iterables
 
def countdown():
  i=0
  while i < 5:
    yield i
    i += 1
    
for i in countdown():
  print(i)
	
	


	
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()


#maps
def add_five(x):
  return x + 5

nums = [2,3,4,5]
result = list(map(add_five, nums))
print(result)
#filter
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)#a function that return boolean


#factorial

def factorial(x):
	if x==1:
		return x
	else:
		return x * factorial(x-1)
print(factorial(5))


#fibonaci

def fib(x):
	if x==0 or x==1:
		return 1
	else:	
		return fib(x-1)+ fib(x-2)
print(fib(4))

#sets

#itertools

#OOPS
	

