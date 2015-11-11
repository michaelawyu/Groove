from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/test')
def test():
	testList=[42,50,12,25,26,37]
	return render_template('test.html',testList=testList)

if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0')