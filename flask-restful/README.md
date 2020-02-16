#FLASK - Python micro web frame work

#installation in miniconda
>> conda install flask #web frame work
>>conda install flask-wtf #WTF form 


from flask import Flask

app=Flask(__name__)

@app.route('/',method=['GET'])
def hello():
    return 'Hello world'
   
app.run()

