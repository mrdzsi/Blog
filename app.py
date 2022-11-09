from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/browse')
def browse():
    return render_template("browse.html")


@app.route('/swipe')
def swipe():
    return render_template("swipe.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<name>')
def user(name):
    return render_template("user.html",
                            user_name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)