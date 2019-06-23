# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: 
# Consider use range(#begin, #end) method


# print("Program starts from here")
# l=[]
# for i in range(2000,3201):
	# if (i%7==0) and (i%5 !=0):
		# l.append(str(i))




# def fact(facto):
	# if(facto==1):
		# return facto
	# else:
		# return facto*(fact(facto-1))

# print(fact(5))

class Employee:
	def __init__(self,name,exp,age):
		self.name=name
		self.exp=exp
		self.age=age
		self.email=name + '@company.com'
emp1=Employee("Ved",2.5,25)
emp2=Employee("Guru",15,40)
emp3=Employee("Ahmed",7,33)
	
print(emp1.name)
print(emp1.email)

print(emp2.name)
print(emp3.name)
