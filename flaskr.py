from flask import Flask, render_template, g, request, redirect, url_for
from sqlalchemy import *
#'cy2415:345@w4111db1.cloudapp.net:5432/proj1part2'
engine = create_engine('sqlite:///testDB.db')

app = Flask(__name__)
global filterList
filterList=[]
global dataSet
dataSet=[]
global colorSet
colorSet=['','','','','','']

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/music')
def music():
	global filterList
	global dataSet
	filterList=[]
	dataSet=[]
	return render_template('music.html')

@app.route('/music', methods=['POST'])
def updatemMusicFilter():
	global filterList
	global dataSet
	if filterList.count(str(request.form['checked']))==0:
		filterList.append(str(request.form['checked']))
		cur=g.conn.execute('SELECT test.value FROM test WHERE test.name="'+str(request.form['checked'])+'"')
		tmpList=cur.fetchall()
		dataList=[]
		numberList=[]
		for item in tmpList:
			dataList.append(item[0])
		dataSet.append(dataList)
	i=0
	while i<len(filterList):
		numberList.append(i)
		i=i+1
	return render_template('musicwfilter.html',filterList=filterList,dataSet=dataSet,numberList=numberList)

@app.route('/music/add')
def addFilterByMusicTitle():
	cur=g.conn.execute('SELECT DISTINCT test.name FROM test')
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