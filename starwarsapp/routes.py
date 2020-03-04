from flask import url_for, request, render_template
from starwarsapp import app

@app.route("/")
def index():
    return render_template('index.html')