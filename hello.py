from flask import Flask,url_for, session, escape, request, redirect, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('login.html', name=name)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s <p> <a href="/logout"> logout</a>' % escape(session['username'])
    return 'You are not logged in <p> <a href="/login"> login 하러가기</a>'

'''
@app.route('/student/<username>/')
def student(username):
	return 'Hello %s' % username
'''

@app.route('/student/<username>/<int:user_id>')
def student(usename,user_id):
	return 'Hello %s , $d' % (username, user_id)

@app.route('/method' , methods=['GET','POST'])
def test_HTTP_method():
	if request.method == 'POST':
		return request.method
	else:
		return request.method + '<p>' + request.args.get('name') + '<p>' + request.args.get('password')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/login', methods=['POST','GET'])
def login():
	try:
		if request.method  == "POST" :  
			name	= request.form['name']
			passwd	= request.form['password2']
			if name : 
				session['username'] = name
			return "%s logged-in " % name
			return redirect(url_for('index'))
	
		else : 
			return render_template('login.html')

	except KeyError, err:
		print 'error-> : ', err
		return '!!!ERROR!!!ERROR!!!ERROR!!!ERROR!!!\n'


if __name__ == '__main__':
	app.debug = True
	app.secret_key = '\x02$\x83U\x9a\xbf\x19\xac8oO^\xf7\x98\xd9\x95.B;(\xe2\x9a,N'
	app.run()

