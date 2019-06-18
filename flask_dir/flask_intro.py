from flask import Flask,render_template
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8889484a601e14bd086580ca86ec1262'
posts=[
	{'Universe':'Star Wars',	 
	 'Movie':'Star Wars II',	 
	 'Title':'Attack of clones',
	 'Director':'George Lucas'	
	},
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
	

	
if __name__ =="__main__":
	app.run(debug=True)