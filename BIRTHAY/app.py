from flask import Flask, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scene/<int:n>")
def scene(n):
    try:
        return render_template(f"scenes/scene{n}.html")
    except TemplateNotFound:
        return "Scene not found", 404

if __name__ == "__main__":
    app.run(debug=True)
