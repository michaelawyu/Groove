from flask import Flask, render_template
from sqlalchemy import *

app = Flask(__name__)
engine = create_engine('sqlite:////testDB.db')

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
	testList=engine.execute('SELECT test.value FROM test')
	return render_template('test.html',testList=testList)

if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0')