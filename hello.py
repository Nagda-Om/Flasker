from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# create route decorator
@app.route('/')
def index():
    first_name="john"
    stuff = "This is <strong>Bold</strong>"
    favorite_pizza = ["Pepproni","cheeze","macroni", 42]
    return render_template('index.html',first_name=first_name, stuff=stuff,favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)



''' Filters
safe
capitalize
lower
upper
title
trim
striptags
'''


## Create Custom Error Page

# invalid URL 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error 504 thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template('504.html'), 500