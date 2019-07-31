import re

x= " iounjwkj nqwjn wkj clk1"

y=re.search("[0-9]{4}-[0-9]{2}",x)
print(y)


try:
	print(4/0)
except :
	print("exception occured")
	
	
def naivesum(list):
	s=0
	for i in list:
		s+=i
	return s
print(naivesum([1,2,3,4]))

