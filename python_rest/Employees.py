#import flask
from flask import Flask,request,jsonify
from flask_restful import Resource,Api
from sqlalchemy import create_engine
from json import dumps

db_connect=create_engine('sqlite:///chinook.db')
app=Flask(__name__)
api=Api(app)

class Employees(Resource):
	def get(self):
		conn=db_connect.connect() #create connection to DB
		query =conn.execute("SELECT * FROM EMPLOYEES")	#perform query and return json result
		return{'employees': [i[0]for i in query.cursor.fetchall()]}
class Tracks(Resource):
	def get(self):
		conn=db_connect.connect() #create connection to DB
		query =conn.execute("select trackid,name,composer,unitprice from tracks where trackid<5;")	#perform query and return json result
		result={'data':[dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
		return jsonify(result)
		
api.add_resource(Employees,'/employees')	
api.add_resource(Tracks,'/data')	

if __name__=='__main__':
	app.run(port='5002',debug=True)

		