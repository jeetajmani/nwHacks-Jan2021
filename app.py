from flask import  Flask, render_template, url_for, redirect, request, send_file
from flask_sqlalchemy import SQLAlchemy
''' create instance of Flask web app '''
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
db.create_all()

''' The decoration is to give a route to Flask to access this method '''
''' in the route parameter is to give a path to the method (web query) '''
@app.route("/")
def home():
    incomplete = Item.query.filter_by(complete=False).all()
    return render_template('home.html', incomplete=incomplete)

@app.route('/add', methods=['POST'])
def add():
    item = Item(text=request.form['items'], complete=False)
    db.session.add(item)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/complete', methods=['POST'])
def complete():
    id = request.form.get('id')
    item = Item.query.filter_by(id=int(id)).first()
    item.complete = True
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
