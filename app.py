from flask import Flask, redirect, url_for, request, render_template, abort, jsonify
from helper import read_csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success/<name>/')
def success(name):
    return 'welcome %s' % name

# serving json request from android app
@app.route('/Androidlogin/', methods=['POST'])
def Androidlogin():
    if request.method == 'POST':
        data = request.get_json()
        user = data['uname']
        password = data['psw']

        if read_csv(user, password):
            return jsonify({'result': 'succcess'})

        else:
            return jsonify({'result': 'failed'})

# serving form request from website
@app.route('/Weblogin/', methods=['POST'])
def Weblogin():
    if request.method == 'POST':
        user = request.form['uname']
        password = request.form['psw']

        if read_csv(user, password):
            return redirect(url_for('success', name=user))
        else:
            abort(401)


if __name__ == '__main__':
    app.run(debug=True)
