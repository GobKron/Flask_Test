from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("homePage.html")

@app.route('/f1')
def forumla():
    return render_template("formula1.html")

@app.route("/weather")
def weather():
    return render_template("weather0.html")


if __name__ == "__main__":
    app.run(debug=True)
