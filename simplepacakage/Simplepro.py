from datetime import datetime
import random

class Simplepro:
	s=0
	def __init__(self):
		x=datetime.now();
		print(x)
	def sumof(self,x):
		
		for i in range(x):
			x=random.randint(1,10)
			if x == i:
				print("I am too old for that shit!!")
				break
		return i
