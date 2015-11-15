from flask import Flask, render_template, g, request, redirect, url_for
from sqlalchemy import *
#'cy2415:345@w4111db1.cloudapp.net:5432/proj1part2'
engine = create_engine('cy2415:345@w4111db1.cloudapp.net:5432/proj1part2')

app = Flask(__name__)
global filterList
filterList=[]
global dataSet
dataSet=[]
global colorSet
colorSet=[
"rgba(0,191,255,",
"rgba(30,144,255,",
"rgba(100,149,237,",
"rgba(135,206,235,",
"rgba(70,130,180,",
"rgba(176,224,230,"
]

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
	global colorSet
	if filterList.count(str(request.form['checked']))==0:
		filterList.append(str(request.form['checked']))
		cur=g.conn.execute('SELECT RANK.rank_number FROM RANK, Music WHERE RANK.mid = Music.mid AND Music.name="'+str(request.form['checked'])+'"')
		tmpList=cur.fetchall()
		dataList=[]
		
		for item in tmpList:
			dataList.append(item[0])
		dataSet.append(dataList)
	numberList=[]
	i=0
	while i<len(filterList):
		numberList.append(i)
		i=i+1
	return render_template('musicwfilter.html',filterList=filterList,dataSet=dataSet,numberList=numberList,colorSet=colorSet)

@app.route('/music/add')
def addFilterByMusicTitle():
	cur=g.conn.execute('SELECT DISTINCT Music.name FROM Music')
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