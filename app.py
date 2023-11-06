from flask import Flask
from routes.cars import cars_bp
from routes.customers import customers_bp
from routes.employees import employees_bp
from routes.orders import orders_bp

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Dette er startsiden for Flask-appen."

app.register_blueprint(cars_bp, url_prefix='/cars')
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(employees_bp, url_prefix='/employees')
app.register_blueprint(orders_bp, url_prefix='/orders')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)











