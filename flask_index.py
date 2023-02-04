from flask import Flask, render_template
app = Flask(__name__)
@app.route("/index")
def first_webPage():
    name = "Flask"
    return render_template("index.html", index_variable = name)
app.run(debug=True)
