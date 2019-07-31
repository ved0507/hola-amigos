class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age=0
        if initialAge > 0:
            self.age=initialAge
        else:
            print("Age is not valid Setting age to 0")      
        

    def amIOld(self):
        if (age < 13):
            print("You are Young")
        elif (age>=13) and (age<18):
            print("You are a teenager")
		else:
			print("You are old")

        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        global age
        # Increment the age of the person in here
        age=age+1



t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")