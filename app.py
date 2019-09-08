from flask import Flask, redirect, url_for, request, render_template, abort, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success/<name>/')
def success(name):
    return 'welcome %s' % name


@app.route('/login/', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = data['uname']
        password = data['psw']

        if user == 'admin' and password == 'admin':
            return jsonify({'result': 'succcess'})
            # return redirect(url_for('success', name=user))

        else:
            return jsonify({'result': 'failed'})

# serving form request from website
# @app.route('/login/', methods=['POST'])
# def login():
#     if request.method == 'POST':
#         user = request.form['uname']
#         password = request.form['psw']
#         if user == 'admin' and password == 'admin':
#             return redirect(url_for('success', name=user))
#         else:
#             abort(401)


if __name__ == '__main__':
    app.run(debug=True)
