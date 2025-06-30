from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')


def index():
    card_data = (
        ("What is Google", "Google is a powerful search engine that helps users find information quickly and efficiently. From websites and images to news and videos, Google organizes the world data to make it accessible at the click of a button.", "BUtton text", "static/images/card_image1.png", "/whatisgoogle", "enabled"),
        ("Why use google", "Google offers fast, reliable, and comprehensive search results, making it easy to find exactly what you need. Its user-friendly interface and advanced algorithms ensure you get the most relevant information in seconds.", "BUtton text", "static/images/card_image2.png", "/whyusegoogle", "enabled"),
        ("Features and services", "Google provides a wide range of features and services, including Gmail, Google Maps, Google Drive, and YouTube. These tools help users communicate, navigate, store files, and access entertainment, all seamlessly integrated with your Google account.", "BUtton text", "static/images/card_image4.png", "/featuresandservices", "enabled")
    )
    return render_template("index.html", cards=card_data), 200

@app.route('/contact')
def contact():
    return render_template("contact.html"), 200

# cards info

@app.route('/whatisgoogle')
def whatisgoogle():
    return render_template("whatisgoogle.html"), 200

@app.route('/whyusegoogle')
def whyusegoogle():
    return render_template("whyusegoogle.html"), 200

@app.route('/features')
def features():
    return render_template("features.html"), 200

# steps

@app.route('/steps')
@app.route('/help')
def steps():
    return render_template("steps.html"), 200

@app.route('/steps/intro')
def steps_intro():
    return render_template("/steps/intro.html"), 200

@app.route('/steps/1')
def steps_1():
    return render_template("/steps/step_1.html"), 200

@app.route('/steps/2')
def steps_2():
    return render_template("/steps/step_2.html"), 200

@app.route('/steps/3')
def steps_3():
    return render_template("/steps/step_3.html"), 200

@app.route('/steps/4')
def steps_4():
    return render_template("/steps/step_4.html"), 200

@app.route('/steps/5')
def steps_5():
    return render_template("/steps/step_5.html"), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template("pagenotfound.html"), 404



if __name__ == '__main__':
    app.run(debug=True)