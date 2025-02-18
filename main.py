from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_word():
    return render_template("index.html"), 200

if __name__ == '__main__':
    app.run(debug=True)