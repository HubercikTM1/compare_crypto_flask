from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "POST":
        return redirect(url_for("graph"))
    else:
        return render_template('main.html')


@app.route('/graph', methods=["POST", "GET"])
def graph():
    fc = request.form["fc"]
    sc = request.form["sc"]

    return render_template("graph.html",fc=fc,sc=sc)


if __name__ == '__main__':
    app.run(debug=True)