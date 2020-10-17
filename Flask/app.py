from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('form.html')


@app.route('/thanks', methods=["GET"])
def get_thanks():
    return render_template('ok.html')

@app.route('/thanks', methods=["POST"])
def thanks():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(name + ' | ' + email)
    print(message)
    return redirect(url_for('get_thanks'))

app.run(debug=True)