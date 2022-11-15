import csv

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>This is the home page!</p>"
