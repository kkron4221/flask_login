from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['id'] == 'login' and request.form['pwd'] == 'pass':
            return render_template('result.html', login_name = request.form['id'])
        else:
            return render_template('index.html', err_message = 'ログイン名かパスワードもしくはその両方が間違っています')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port = 8000, debug=True)
