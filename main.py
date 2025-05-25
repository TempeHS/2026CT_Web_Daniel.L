from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')

def index():
    card_data = (
        ("What is Google", "Google is a powerful search engine that helps users find information quickly and efficiently. From websites and images to news and videos, Google organizes the world data to make it accessible at the click of a button.", "BUtton text", "static/images/card_image1.png"),
        ("Why use google", "Description", "BUtton text", "static/images/card_image2.png"),
        ("Features and services", "Description", "BUtton text", "static/images/card_image3.png"),      
    )
    return render_template("index.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)