# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect
from forms import QueryForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/", methods=["GET", "POST"])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        result_url = "/val={}".format(form.number.data)
        return redirect(result_url)
    return render_template("index.html", form=form)

@app.route("/val=<num>")
def square(num):
    _num = float(num)
    return "Square of {} = {}".format(_num, _num*_num)
    
if __name__ == "__main__":
    app.run()