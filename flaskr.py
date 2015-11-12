from flask import Flask, render_template
from sqlalchemy import *

app = Flask(__name__)
engine = create_engine('sqlite:////testDB.db')
conn = engine.connect()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/music')
def music():
	return render_template('music.html')

@app.route('/test')
def test():
	testList=[42,50,12,25,26,37]
	return render_template('test.html',testList=testList)

if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0')