from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Sample data for demonstration (you could load your dataset here)
data_path = "./data/processed/sales.csv"
df = pd.read_csv(data_path)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
