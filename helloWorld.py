'''Welcome to python 101'''

##a,e
a=2
b="vedavyas"
c=3.1423456789
d=True
print(a)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
##b
p=q=r=s=t=45
print(p)
print(q)
print(r)
print(s)
print(t)
##c
'''import keyword
print(keyword.kwlist)
True False break class continue def elif finally for while
and return'''
##d
print(id(p))
print(id(a))
print(id(b))
##f
a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a%b)
'''Types of format 
positinal - {1} {0} {2}.format("c","b","a")
keyword - {c} {a} {b}.format(a='apple',b='ball',c='cat')
'''
#format()
str="This is NIA automation {}"
print (str.format("Team"))
##multiple format()
my_string = "{1}, or  {0} there is No {2}"
print (my_string.format("Do", "Dont", "Try"))


#concatinate string

str3="ved"
str4="vyas"
print(str3+str4)
print(str3*3)
print(str3+3) #error
print(str3+str(3)) #error


#List

#create a list and tuple print it

list1=[12,23,45,67,12]
tuple1=("Pune","Mumbai","Chennai")
#print the list and tuple
print(list1)
print(tuple1)
#count of list and tuple
print(list1.count(12))
print(tuple1.count("Mumbai"))

#length of tuple and list
print("\nprinting the length of list and tuple: ")
print(len(list1))
print(len(tuple1))

#copy of both and print the copy
print("\ncreating copy of list & tuple and printing the copy")
list1_copy=list1
tuple1_copy=tuple1
print(list1_copy)
print(tuple1_copy)

list1=[12,23,45,67,12]
tuple1=("Pune","Mumbai","Chennai")
#append the value to list1
list1.append(97)
print(list1)
#insert the value to list1
list1.insert(2,34)
print(list1)
#pop the value to list1
list1.pop(3)
print(list1)

#Removal of First Element
print("\nRemoval of First Element: ") 
print(tuple1[1:]) 
#delete tuple
print("\nDelete tuple")
del tuple1
print(tuple1)

list1=[12,23,45,67,12]
tuple1=("Pune","Mumbai","Chennai")
#print the list and tuple
print(list1)
print(tuple1)
print(list1[2])
print(tuple1[1])
list1.sort()
#tuples are immutable in nature
#tuple1[0]=13
#list is mutable in nature
list1[1]=13
print(list1)
print(tuple1)

#append on list
list1.append(78)
print(list1)
#extend  on list
list1.extend([20,30,40])
print(list1)
#insert to add element on particular position
list1.insert(3,'bengaluru')
print(list1)
#find and fetch the particular value
list1[1]

list1=[12,23,45,67,12]
tuple1=("Pune","Mumbai","Chennai")
print(list1)

print("count of number 12 in list1:")
print(list1.count(12))

print("Remove number 23 in list1:")
list1.remove(23)
print(list1)

print("POP number from position 2 in list1:")
list1.pop(2)
print(list1)
print("del value from  list1:")
del list1[1]
print(list1)
# Hello World program in Python
#Dictionary

#create and perfrom function

dict1={8:'New Delhi',2:'Bengaluru',3:'Pune',4:'Kolkata'}
print(dict1)

#display value of particular key


print(dict1[2])
print(dict1[3])
print(dict1.get(9,"no-keyfound"))

#in operator
print(1 in dict1)
print(8 in dict1)
#add new key value pair

dict1[5]='Chennai'
print(dict1)

dict1.update({6:'Surat', 7:'Hydrabad'})
print("\nadded new key value pair:")
print(dict1)

#modify existing key value pair
print("\nUpdatednew key value pair:")
dict1[7]='Jaipur'
print(dict1)

#delete key value pair from dict1 --we can clear also
print("\nDelete key value pair:")
del dict1[6]
dict1.pop(7)
print(dict1)

#Sort items in the dict1
print("\nSorted list of key value pair:")
print(sorted(dict1))
print(dict1.keys())
print(dict1.values())
print(sorted(dict1.keys()))
print(sorted(dict1.values()))
print(sorted(dict1.items()))

#1.Functions - do nothing print something

def do_nothing():
    print("I was told to do nothing :D")
do_nothing()

#arbitary number of args

def arbitary_args(*args):
    for i in args:
        print(i)
    
print(arbitary_args(1,2,3,4))

#recursive function factiorial function 

def rec_function(x):
    if x==1:
        return 1
    else:
        fact=x*rec_function(x-1)
        return fact
print(rec_function(5))
#  write function assign to variable and use it

def var_func(x):
    if x==1:
        return 1
    elif x%2==0:
        print("Its even")
    else:
        print("Its Odd")
y=var_func(78)
print(y)


'''
1.Classes with field and method

2.Instantite the class and use the object to call the method.

3.Define a class which has asatleast 2 metyhods.getstring:to get 
a string from console input printstring :to print string in upper
case.also include simple function to test class method.

4.Write constructr for Class both default and parameterized.

5.Create new class and inherit the class cerated earlier in the class.
'''

class Person:
	def __init__(self,name):
		self.name=name
	def say_my_name(self):
		print("Hello, My name is ",self.name)
p = Person('Vedavyas')
p.say_my_name()

if name = "ved" or name = "vyas":
	print("name is vedavyas")
elif var == 0:
	print "Help  - elif"

#calculate the area of circle
#pi*r**2
#instantite the class and use the object to call the method
# Example for parameterized constructor
import math
class Area_of_object():
	def __init__(self,radius):
		self.radius = radius
	def area_of_circle(self):
		return (math.pi * (self.radius ** 2))
	def area_of_sphere(self):
		return (4 * math.pi * (self.radius ** 2))
		
	def getString(self,str1):
		self.str1 = input("Enter the string: ")
		

circle= Area_of_object(4)
sphere = Area_of_object(4)
print(circle.area_of_circle())
print(sphere.area_of_sphere())

#getString to get the string from console
#printString to print the string in uppercase
#example for default constructor

class strings1:
    
    def getString(self):
        self.str1 = input("Enter the string: \n")
    def printString(self):
        return self.str1.upper()
    def __init__(self):
        pass
one = strings1()
one.getString()
print("printstring fun",one.printString())



#create class and inherit the class

class Football:
    #League player details
    def __init__(self,jersey):
        self.jersey = jersey
    def player_details(self):
        if (self.jersey == 10):
            print("Leo Messi - Barcelona - Spain")
        elif(self.jersey == 11):
            print("Mo Salah - Liverpool - England")
        elif(self.jersey == 7):
            print("Cristiano Ronaldo - Juventus - Italy")
        else:
            print("Try numbers like 7 or 11 or 10")

#inherit the class Fotball in to childclass League
class League(Football):
    def __init__(self):
        Football.__init__(self,10)
    def goalscored(self):
        if (self.jersey == 10):
            print("Scored 15 goals")
        elif(self.jersey == 11):
            print("Scored 10 goals")
        elif(self.jersey == 7):
            print("Scored 14 goals")
        else:
            print("NO goals ")
    
c = League()
c.player_details()
c.goalscored()
	
