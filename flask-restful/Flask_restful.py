from flask import Flask
from flask_restful import Resource ,Api

app=Flask(__name__)
api=Api(app)

class HelloThere(Resource):
	def get(self):
		return {'General':'Kenobi'}
		


class episodeV:
	def get(self,trooper):
		return {trooper:troopers[trooper]}
		

	def put(self,trooper):
		troopers[trooper]=request.form[trooper]
		return {trooper:troopers[trooper]}

api.add_resource(episodeV,'/<string:todo_id>')
		
if __name__=='__main__':
	app.run(debug=True)	
	
	
	
