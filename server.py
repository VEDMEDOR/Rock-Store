from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        print(f"{title}\n{intro}\n{text}\n")
    else:
        return render_template("create-article.html")


if __name__ == "__main__":
    app.run(debug=True)