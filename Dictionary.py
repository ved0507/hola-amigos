print("Hello there")


dict={1:"A new hope",2:"Empire strikes back",3:"Return of the Jedi"}
#print out all the key and value 
list1=[]
for key,value in dict.items():
	print(key,":",value)

	
#convert data of dict to list
for key,value in dict.items():
	print(key,":",value)
	list1.append(key)
	list1.append(value)
print(list1)


#--- update the dictionary
dict[1]="Phantom meneace"
print(dict.get(1))
print(dict)

	
#=== sololearn questions

def numbers(x):
	for i in range(x):
		if i % 4 == 3:
			yield i
			print(i)
list(numbers(11))
#ans==> 3,7


def add(x,y):
	x+y
	return 0
print(5+6,0)


fruits =["apples","oranges","lemons"]
fruits[2] = "strawberries"
print(fruits)
print(fruits[2][5:])



#lex_auth_012693774187716608134

def translate(bilingual_dict,english_words_list):
    #Write your logic here
	swedish_words_list=[]
	for  key,value in bilingual_dict.items():
	    if key in english_words_list:
		    swedish_words_list.append(value)
    #print(swedish_words_list)
	return swedish_words_list


bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas"]
#english_words_list=translate(bilingual_dict, english_words_list)
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)

#======== set 
flight_set={500,520,600,345,520,634,600,500,200,200}

print(flight_set)

passengers_list=["George", "Annie", "Jack", "Annie", "Henry", "Helen", "Maria", "George", "Jack", "Remo"]
print(set(passengers_list))
