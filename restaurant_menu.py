from flask import Flask
import sqlite3


app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    # return "This page will show all my restaurants"
    db = sqlite3.connect('restaurant_menu.db')
    cursor = db.cursor()
    items = cursor.execute('SELECT name FROM restaurant').fetchall()
    db.close()
    # print(itmes)
    # return 'hohoho'
    mydoc = "<h1>All Restaurants</h1>"
    mydoc += "<ul>"
    for item in items:
        mydoc += f"<li>{item[0]}</li>"
    mydoc += "</ul>"
    return mydoc

@app.route('/restaurant/new/')
def newRestaurant():
    return "This page whill be for making a new restaurant"

@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return f"This page will be for deleting restaurant {restaurant_id}"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)