from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')

def index():
    card_data = (
        ("What is Google", "Google is a powerful search engine that helps users find information quickly and efficiently. From websites and images to news and videos, Google organizes the world data to make it accessible at the click of a button.", "BUtton text", "static/images/card_image1.png"),
        ("Why use google", "Google offers fast, reliable, and comprehensive search results, making it easy to find exactly what you need. Its user-friendly interface and advanced algorithms ensure you get the most relevant information in seconds.", "BUtton text", "static/images/card_image2.png"),
        ("Features and services", "Google provides a wide range of features and services, including Gmail, Google Maps, Google Drive, and YouTube. These tools help users communicate, navigate, store files, and access entertainment, all seamlessly integrated with your Google account.", "BUtton text", "static/images/card_image4.png")
    )
    return render_template("index.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)