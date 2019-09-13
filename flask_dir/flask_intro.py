
from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SECRET_KEY'] = '8889484a601e14bd086580ca86ec1262'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email = db.Column(db.String(120),unique=True,nullable=False)
	image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
	password =db.Column(db.String(60),nullable=False)
	posts = db.relationship('Post',backref='Movie',lazy=True)
	
	def __init__(self):
		pass
	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(100),nullable=False)
	date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	content = db.Column(db.Text,nullable=False)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"
posts=[
	
	{'Universe':'Star Wars',	 
	 'Movie':'Star Wars V',	 
	 'Title':'Empire Strikes Back',
	 'Director':'Irvin Kershner'	
	},
	{'Universe':'Star Wars',	
	 'Movie':'Star Wars VII',	 
	 'Title':'The Force Awakens',
	 'Director':'JJ Abram'	
	}
]
@app.route("/")
@app.route("/home")
def hello():
    return render_template("homepage.html",posts=posts)
	
@app.route("/about")
def about():
    return render_template("aboutpage.html",Universe='About General Kenobi')

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html',title='register', form=form)
	
@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html',title='login', form=form)
	
	
if __name__ =="__main__":
	app.run(debug=True)
	
