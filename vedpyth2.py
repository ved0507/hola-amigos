# print("Hell o")

# x1=(lambda x,y,z: (x+y)*z)(1,2,7)
# print(x1)

# y1=(lambda x,y,z: (x+y) if (z==0)  else (x*y))(1,2,0)
# print(y1)
# print(type(y1))




# nums=[99,22,33,141,112,134,189,312,54,89]
# def Key(x):
	# return x%2
# print(nums)
# print(sorted(nums ,key=Key))



# x1=(lambda x: "one" if x==1 else ("Two" if x==2 else "three"))(2)
# print(x1)

# #1 
# a= ["vedavyas","p","Burli"]

# print(" ".join(a))
# #2 in place swapping
# x,y=20,30
# print(x,y)
# x,y=y,x
# print(x,y)

# #3 reversing a string
# b="Lord Darth Vader"
# print(b[::-1])

# def multiply(a, b):
    # return a * b
# p=multiply(1,2)
# print(p)


# list1=[1,2,3,4]
# print(list1)
# list1.append(2)
# print(list1)


# def unique_in_order(iterable):	
	# list1=[]
	# for i in range(len(iterable)-1):		
		# print(i,iterable[i])
		# if iterable[i] != iterable[i+1]:
			# print(iterable[i])
			# list1.append(iterable[i])
			
	# print(list1)
# unique_in_order("AAAABBBCCDAABBB")


from flask import Flask
from flask_restful import Resourse,Api
print("imported")

app=Flask(__name__)
api=Api(app)

#class TestApi(Resource):
@app.route("/")
@app.route("/login")

def hello():
	return ("Hello world")
	
	
	

if __name__=="__manin__":
	app.run(port=5000,debug=True)


print("flask imported")