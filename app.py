from flask import  Flask, render_template, url_for, redirect, request, send_file
from flask_sqlalchemy import SQLAlchemy
import recipe

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
    ID = request.form.get('id')
    item = Item.query.filter_by(id=int(ID)).first()
    item.complete = True
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/topDishes')
def topDishes():

    dishes = top_dish_helper()

    urls = []

    for x in dishes:
        urls.append(recipe.thumbnail(x["link"]))

    print(urls)

    return render_template('recipe.html', dishes=dishes, urls=urls)

@app.route('/display/<name>')
def display(name):

    dish = recipe.reverse_lookup(name)
    print(dish)
    return render_template('display.html', dish=dish)







def top_dish_helper():
    incomplete = Item.query.filter_by(complete=False).all()
    ing = []
    for i in incomplete:
        ing.append(i.text)
    dishes = recipe.recipe_find(ing)

    return dishes




if __name__ == '__main__':
    app.run(debug=True)
