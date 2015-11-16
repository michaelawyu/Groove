from flask import Flask, render_template, g, request, redirect, url_for
from sqlalchemy import *
#'postgresql://cy2415:345@w4111db1.cloudapp.net:5432/proj1part2'
engine = create_engine('postgresql://cy2415:345@w4111db1.cloudapp.net:5432/proj1part2')

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

@app.route('/medium')
def medium():
	global filterList
	global dataSet
	filterList=[]
	dataSet=[]
	return render_template('medium.html')

@app.route('/medium', methods=['POST'])
def updateMediumFilter():
	global filterList
	global dataSet
	global colorSet
	if filterList.count(str(request.form['checked']))==0:
		muTitleList=[]
		someOfRanks=[0,0,0,0,0,0]
		filterList.append(str(request.form['checked']))
		cur=g.conn.execute('SELECT Music.mid FROM Music, STORED_ON, Medium WHERE Music.mid = BELONGS_TO.mid AND BELONGS_TO.medium_type = Medium.medium_type AND Medium.medium_type='+"'"+str(request.form['checked'])+"'")
		tmplist2=cur.fetchall()
		for item in tmplist2:
			muTitleList.append(item[0])
		for item in muTitleList:
			cur=g.conn.execute('SELECT RANK.rank_number FROM RANK, Music WHERE RANK.mid = Music.mid AND Music.mid='+"'"+str(item)+"'")
			tmplist2=cur.fetchall()
			i=0
			while i<6:
				someOfRanks[i]=someOfRanks[i]+tmplist2[i][0]
				i=i+1
		
		dataSet.append(someOfRanks)
	
	numberList=[]
	i=0
	while i<len(filterList):
		numberList.append(i)
		i=i+1
	return render_template('mediumwfilter.html',filterList=filterList,dataSet=dataSet,numberList=numberList,colorSet=colorSet)

@app.route('/medium/add')
def addFilterByMedium():
	cur=g.conn.execute('SELECT DISTINCT Medium.medium_type FROM Artist')
	titleList=[]
	resultList=cur.fetchall()
	for tuple in resultList:
		titleList.append(str(tuple[0]))
	return render_template('addfilterme.html',titleList=titleList)

@app.route('/pd')
def pd():
	global filterList
	global dataSet
	filterList=[]
	dataSet=[]
	return render_template('pd.html')

@app.route('/pd', methods=['POST'])
def updatePDFilter():
	global filterList
	global dataSet
	global colorSet
	if filterList.count(str(request.form['checked']))==0:
		muTitleList=[]
		someOfRanks=[0,0,0,0,0,0]
		filterList.append(str(request.form['checked']))
		cur=g.conn.execute('SELECT Music.mid FROM Music, Production_Company WHERE Music.puid = Production_Company.puid AND Production_Company.name='+"'"+str(request.form['checked'])+"'")
		tmplist2=cur.fetchall()
		for item in tmplist2:
			muTitleList.append(item[0])


		for item in muTitleList:
			cur=g.conn.execute('SELECT RANK.rank_number FROM RANK, Music WHERE RANK.mid = Music.mid AND Music.mid='+"'"+str(item)+"'")
			tmplist2=cur.fetchall()
			i=0
			while i<6:
				someOfRanks[i]=someOfRanks[i]+tmplist2[i][0]
				i=i+1
		
		dataSet.append(someOfRanks)
	
	numberList=[]
	i=0
	while i<len(filterList):
		numberList.append(i)
		i=i+1

	return render_template('pdwfilter.html',filterList=filterList,dataSet=dataSet,numberList=numberList,colorSet=colorSet)


@app.route('/pd/add')
def addFilterByPD():
	cur=g.conn.execute('SELECT DISTINCT Production_Company.name FROM Production_Company')
	titleList=[]
	resultList=cur.fetchall()
	for tuple in resultList:
		titleList.append(str(tuple[0]))
	return render_template('addfilterpd.html',titleList=titleList)

@app.route('/artist')
def artist():
	global filterList
	global dataSet
	filterList=[]
	dataSet=[]
	return render_template('artist.html')

@app.route('/artist', methods=['POST'])
def updateArtistFilter():
	global filterList
	global dataSet
	global colorSet
	if filterList.count(str(request.form['checked']))==0:
		muTitleList=[]
		someOfRanks=[0,0,0,0,0,0]
		filterList.append(str(request.form['checked']))
		cur=g.conn.execute('SELECT Music.mid FROM Music, CREATED_BY, Artist WHERE Music.mid = CREATED_BY.mid AND CREATED_BY.auid = Artist.auid AND Artist.name='+"'"+str(request.form['checked'])+"'")
		tmplist2=cur.fetchall()
		for item in tmplist2:
			muTitleList.append(item[0])
		for item in muTitleList:
			cur=g.conn.execute('SELECT RANK.rank_number FROM RANK, Music WHERE RANK.mid = Music.mid AND Music.mid='+"'"+str(item)+"'")
			tmplist2=cur.fetchall()
			i=0
			while i<6:
				someOfRanks[i]=someOfRanks[i]+tmplist2[i][0]
				i=i+1
		
		dataSet.append(someOfRanks)
	
	numberList=[]
	i=0
	while i<len(filterList):
		numberList.append(i)
		i=i+1
	return render_template('artistwfilter.html',filterList=filterList,dataSet=dataSet,numberList=numberList,colorSet=colorSet)

@app.route('/artist/add')
def addFilterByArtist():
	cur=g.conn.execute('SELECT DISTINCT Artist.name FROM Artist')
	titleList=[]
	resultList=cur.fetchall()
	for tuple in resultList:
		titleList.append(str(tuple[0]))
	return render_template('addfilterar.html',titleList=titleList)

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
		cur=g.conn.execute('SELECT RANK.rank_number FROM RANK, Music WHERE RANK.mid = Music.mid AND Music.name='+"'"+str(request.form['checked'])+"'")

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