from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Sample data for demonstration (you could load your dataset here)
data_path = "./data/processed/sales.csv"
df = pd.read_csv(data_path)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    return render_template("index.html")


@app.route("/get_plot", methods=["GET", "POST"])
def get_plot():
    if request.method == "POST":
        plt.plot([1, 2, 3])
        plt.title("Line Plot")
        plt.show()
        plt.savefig("static/line_plot.png")
        return render_template("index.html", plot_url="static/line_plot.png")
    else:
        pass


### Get the natural language input
@app.route("/get_nl_input", methods=["GET", "POST"])
def get_nl_input():
    if request.method == "POST":
        nl_input = request.form["nl_input"]
        print(nl_input)
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
