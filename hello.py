from flask import Flask, render_template

#create flask instance
app = Flask(__name__)

@app.route('/')
def index():
    first_name = 'John'
    stuff = 'This is bold text'
    favourite_pizza = ['pepperoni', 'mushrooms', 'salami', 41]
    return render_template('index.html', name = first_name,
                           stuff=stuff,
                           favourite_pizza=favourite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500