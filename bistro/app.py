from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def bistro_start():
    return render_template('index.html')


@app.route("/recipes")
def recipe_page():
    return render_template('recipes.html')
