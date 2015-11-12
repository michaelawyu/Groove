from flask import Flask, render_template, g
from sqlalchemy import *
#'cy2415:345@w4111db1.cloudapp.net:5432/proj1part2'
engine = create_engine('sqlite:///testDB.db')

app = Flask(__name__)

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
	cur=g.conn.execute('SELECT test.value FROM test')
	testList=cur.fetchall()
	return render_template('test.html',testList=testList)

@app.before_request
def before_request():
	g.conn=engine.connect()

@app.teardown_request
def teardown_request():
	g.conn.close()
	
if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0')