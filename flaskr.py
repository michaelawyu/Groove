from flask import Flask, render_template, g
import sqlite3

#configuration
DATABASE = '/testDB.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

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
	g.db=connect_db()
	cur=g.db.execute('SELECT test.value FROM test')
	testList=cur.fetchall()
	return render_template('test.html',testList=testList)


if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0')