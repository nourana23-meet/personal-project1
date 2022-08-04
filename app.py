from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

config = {

  "apiKey": "AIzaSyB8uuzWFzQPnv2lIkflDtFQpwPjFqmE-zU",

  "authDomain": "personal-project-y2-summ-c8a89.firebaseapp.com",

  "projectId": "personal-project-y2-summ-c8a89",

  "storageBucket": "personal-project-y2-summ-c8a89.appspot.com",

  "messagingSenderId": "934419825773",

  "appId": "1:934419825773:web:c6737a0d4dfc0edac3eb64",

  "measurementId": "G-KXBES38WB9",

  "databaseURL": "https://personal-project-y2-summ-c8a89-default-rtdb.europe-west1.firebasedatabase.app/"
  }


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['SECRET_KEY'] = '252548527'


@app.route('/',methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		Name = request.form['name']
		Bio = request.form['bio']
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			user = {"name": Name, "bio": Bio}
			db.child("usera").child(login_session['user']['localId']).set(user)
			return redirect(url_for('Home'))
		except:
			return render_template('signin.html')
	return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']			
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			return redirect(url_for('Home'))
		except:
			error = "Authentication failed"
	return render_template("signup.html")


@app.route("/product")
def Product():
	return render_template("product.html")


@app.route('/home')
def Home():
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug = True)