from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def Home():
	return render_template('signin.html')




if __name__ == '__main__':
	app.run(debug = True)