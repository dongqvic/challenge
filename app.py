import datetime
import os

from flask import Flask, render_template, redirect, url_for, request
from forms import ItemForm
from models import Items
from database import db_session, init_db

app = Flask(__name__)
# app.secret_key = os.environ['APP_SECRET_KEY']
app.secret_key = 'super_duper_secret'

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
            db_session.add(item)
            db_session.commit()
            return redirect(url_for('success'))
        else:
            return "Validation Failed!!"
    return render_template('index.html', form=form)

@app.route("/success")
def success():
    results = []
    qry = db_session.query(Items)
    results = qry.all()
    arr = []
    for res in results:
        print(vars(res))
        arr.append(vars(res))
    return render_template('table.html', data=arr)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)

