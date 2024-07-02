from flask import Flask, render_template, request
from coffee import Coffee

app = Flask(__name__)

menu = [
    Coffee("Espresso", "Strong and bold coffee.", 1.50),
    Coffee("Latte", "Smooth and creamy coffee.", 2.50),
    Coffee("Cappuccino", "Rich and foamy coffee.", 3.00),
]



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def show_menu():
    return render_template('menu.html', menu=menu)

@app.route('/order', methods=['POST'])
def order():
    coffee_name = request.form.get('coffee')
    coffee = next((c for c in menu if c.name == coffee_name), None)
    if coffee:
        return f"""<center>
<img src="https://avatars.slack-edge.com/2018-09-14/436717422071_715de9f804342c109e0d_512.png" alt="Coffee Image">
<br>
Enjoy your {coffee.name}! {coffee.description}
</center>"""
    return "Invalid coffee selection."

if __name__ == '__main__':
    app.run(debug=True)
