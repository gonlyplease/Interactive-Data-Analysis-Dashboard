from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib
import sqlite3


matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

from langchain_query import nl_to_sql

app = Flask(__name__)

# Sample data for demonstration (you could load your dataset here)
data_path = "./data/processed/sales.csv"
df = pd.read_csv(data_path)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    return render_template("index.html")


"""@app.route("/get_plot", methods=["GET", "POST"])
def get_plot():
    if request.method == "POST":
        plt.plot([1, 2, 3])
        plt.title("Line Plot")
        plt.show()
        plt.savefig("static/line_plot.png")
        return render_template("index.html", plot_url="static/line_plot.png")
    else:
        pass"""

sql_test_query = 'SELECT SUM("gross_income") FROM "branches"'


### Get the natural language input
@app.route("/get_nl_input", methods=["GET", "POST"])
def get_nl_input():
    database_uri = "sqlite:///../sales.db"
    if request.method == "POST":
        nl_input = request.form.get("nl_input")
        sql_query = nl_to_sql(nl_input, database_uri=database_uri)
        print(sql_query)
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
