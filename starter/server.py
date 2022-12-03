from flask import Flask, render_template, url_for, redirect
from cupcakes import read_csv, find_cupcake_csv, find_cupcake, add_cupcake_dictionary, calculate_total

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create_cupcake")
def create_cupcake():
    return render_template('create-cupcake.html')

@app.route("/orders")
def orders():
    return render_template('orders.html', cupcakes = read_csv('current-order.csv'), order_total = round(calculate_total('current-order.csv'), 2))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("display.csv", name)

    if cupcake:
        add_cupcake_dictionary('current-order.csv', cupcake)
        return redirect(url_for('cupcakes'))
    else:
        return "Sorry, cupcake not found"

@app.route("/remove-cupcake/<name>")
def remove_cupcake(name):
    return "cupcake is removed"
    

@app.route("/cupcakes")
def cupcakes():
    return render_template('cupcakes.html', cupcakes = read_csv('display.csv'))

@app.route("/individual_cupcake")
def individual_cupcake():
    return render_template('individual-cupcake.html', cupcake = find_cupcake_csv('display.csv', 'teeny Cake'))

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")
