from flask import Flask, render_template, g, request, redirect, url_for
from sqlalchemy import *
#'cy2415:345@w4111db1.cloudapp.net:5432/proj1part2'
engine = create_engine('sqlite:///testDB.db')

app = Flask(__name__)
filterList=[]
dataList=[]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/music')
def music():
	titleList=[]
	return render_template('music.html')

@app.route('/music', methods=['POST'])
def updatemMusicFilter():
	filterList.append(str(request.form['checked']))
	tmpList=g.conn.execute('SELECT test.value FROM test WHERE test.name=A')
	render_template('test.html',testList=tmpList)
	#return render_template('musicwfilter.html',filterList=filterList)

@app.route('/music/add')
def addFilterByMusicTitle():
	cur=g.conn.execute('SELECT test.name FROM test')
	titleList=[]
	resultList=cur.fetchall()
	for tuple in resultList:
		titleList.append(str(tuple[0]))
	return render_template('addfiltermu.html',titleList=titleList)

@app.route('/test')
def test():
	testList=[0,0,0,0,0,0]
	return render_template('test.html',testList=testList)

@app.before_request
def before_request():
	g.conn=engine.connect()

@app.teardown_request
def teardown_request(exception):
	if g.conn is not None:
		g.conn.close()

if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0')