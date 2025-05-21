from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')

def index():
    card_data = (
        {"What is Google", "Description", "BUtton text", "static/images/card_image1.png"},
        {"Why use google", "Description", "BUtton text", "static/images/card_image2.png"},
        {"", "Description", "BUtton text", "static/images/card_image3.png"},      
    )
    return render_template("index.html"), 200

if __name__ == '__main__':
    app.run(debug=True)