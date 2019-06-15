# import random
# roll="yes"
# while roll=="yes" or roll=="y":
	# print(random.randint(1,6))
	# roll=input("Roll again")
	
# print("Roll game ends here.. Thank you")

#====Gussing game===
# guess_counter=0
# actual_guess=7
# flag="in"
# loop to count the guess and actual guess
# while guess_counter < 5 and flag=="in":
	
	# raw=int(input("Guess the number: "))
	# print(raw)
	
	# if raw == actual_guess:
		# flag="out"
		# print("You guessed it right")
	# guess_counter+=1
	
	
# if guess_counter==5:
	# print("You are out of guesses")
	
string1="vedavyas"

list1=[]
for char in string1:
	print(char)
	list1.append(char)
print(list1[::-1])

length=len(string1)
print(length)
new_str=""
i=0
while length > i:
	print(string1[i])
	i+=1
print(new_str)



