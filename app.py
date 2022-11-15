import csv

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    user_name = request.args.get('name', '')

    with open('pages.csv', 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        context = {
            'name': user_name,
            'pages': csv_reader,
        }

        return render_template('home.html', **context)


@app.route("/page/<pk>/")
def post_detail(pk=None):

    with open('pages.csv', 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row['id'] == pk:
                page = row
                break
        else:
            page = None
            # stops an error from being thrown

        context = {
            'title': page['title'],
            'body': page['body'],
        }

        return render_template('page.html', **context)


@app.route("/hello/")
def hello():
    user_name = request.args.get('name', '')

    context = {
        'name': user_name,
    }
    return render_template('hello.html', **context)


@app.route("/surf-and-paddle/")
def surf_and_paddle():
    return render_template('surf_and_paddle.html')
