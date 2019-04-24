from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login = request.form['id']
        passwd = request.form['pwd']
        if login == 'login' and passwd == 'pass':
            return render_template('result.html', login_name=request.form['id'])
        else:
            return render_template('index.html', message="ログイン名かパスワードもしくはそのどちらも間違ってます")
    else:
        return render_template('index.html', message="ようこそ")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
