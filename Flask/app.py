from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('form.html')

@app.route('/thanks', methods=["POST"])
def thanks():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(name + ' | ' + email)
    print(message)
    return render_template('ok.html')

app.run()