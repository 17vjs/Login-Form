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
        result = read_csv(user, password)
        if result[0]:
            return jsonify(result[1])

        else:
            return jsonify(result[1])

# serving form request from website
@app.route('/Weblogin/', methods=['POST'])
def Weblogin():
    if request.method == 'POST':
        user = request.form['uname']
        password = request.form['psw']
        result = read_csv(user, password)

        if result[0]:
            return redirect(url_for('success', name=result[1]["role"]))
        else:
            abort(401)


if __name__ == '__main__':
    app.run(debug=True)
