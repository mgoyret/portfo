import csv
from flask import Flask, render_template, url_for, request, redirect
from csv import DictWriter
from os.path import getsize


def saveData(data):
    try:
        with open('dataBase.csv', mode='a', newline="") as myFile:
            writerObj = DictWriter(myFile, fieldnames=list(data.keys()))
            if not getsize("dataBase.csv"):
                writerObj.writeheader()
            print(getsize("dataBase.csv"))
            writerObj.writerow(data)
    except TypeError as err:
        print('TYPE ERROR', err)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:sub_page>")
def sub(sub_page):
    return render_template(sub_page)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            print(data := request.form.to_dict())
            saveData(data)
            return redirect("thanks.html")
        except:
            return "did not save to database"
    else:
        return "Error, please try again"
