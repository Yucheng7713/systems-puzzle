import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session

# App initialization
app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

# Route for serving the frontend site
@app.route("/", methods=['GET'])
def front_page():
    return render_template('index.html', form=ItemForm())

# Route for posting new items ( name, quantity, description )
@app.route("/", methods=['POST'])
def add_item():
    form = ItemForm()
    try:
        # If the form is submitted through POST and it's valid
        if form.validate_on_submit():
            item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
            db_session.add(item)
            db_session.commit()
            return redirect(url_for('success'))
        return render_template('index.html', form=form)
    except:
        return "DB session error"

# Route for showing all added items so far - redirect from '/' POST method
@app.route("/success")
def success():
    results = []
    query = ""
    qry = db_session.query(Items)
    results = qry.all()
    return render_template('success.html', results=results)
  

if __name__ == '__main__':
    # The default port running the app is 5000, so we need to change it to port 5001
    app.run(host='0.0.0.0', port=5001, debug=True)
