from flask import Blueprint, request, jsonify
from .cars import cars

orders_bp = Blueprint('orders', __name__)
orders = []


def find_car_by_id(car_id):
    return next((car for car in cars if car['id'] == car_id), None)


def find_order_by_customer_id(customer_id):
    return next((order for order in orders if order['customer_id'] == customer_id and order['status'] == 'bestilt'),
                None)


@orders_bp.route('/order-car', methods=['POST'])
def order_car():
    data = request.get_json()
    car = find_car_by_id(data['car_id'])

    if not car:
        return jsonify({'error': 'Bilen finnes ikke'}), 404

    if car['status'] != 'available':
        return jsonify({'error': 'Bilen er ikke tilgjengelig'}), 400

    existing_order = find_order_by_customer_id(data['customer_id'])
    if existing_order:
        return jsonify({'error': 'Kunden har allerede en bestilt bil'}), 400

    order = {
        'id': len(orders) + 1,
        'car_id': car['id'],
        'customer_id': data['customer_id'],
        'status': 'bestilt'
    }
    orders.append(order)
    car['status'] = 'reserved'

    return jsonify({'message': 'Bil bestilt', 'order': order}), 201


@orders_bp.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    data = request.get_json()
    order = find_order_by_customer_id(data['customer_id'])

    if not order:
        return jsonify({'error': 'Ingen bestilling funnet for denne kunden'}), 404

    car = find_car_by_id(order['car_id'])
    car['status'] = 'available'
    orders.remove(order)

    return jsonify({'message': 'Bestilling avbrutt'}), 200


@orders_bp.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.get_json()
    order = find_order_by_customer_id(data['customer_id'])

    if not order:
        return jsonify({'error': 'Ingen bestilling funnet for denne kunden'}), 404

    car = find_car_by_id(order['car_id'])
    if car['status'] != 'reserved':
        return jsonify({'error': 'Bilen er ikke reservert for utleie'}), 400

    order['status'] = 'leid'
    car['status'] = 'rented'

    return jsonify({'message': 'Bil leid', 'order': order}), 200


@orders_bp.route('/return-car', methods=['POST'])
def return_car():
    data = request.get_json()
    order = next(
        (order for order in orders if order['customer_id'] == data['customer_id'] and order['status'] == 'leid'), None)

    if not order:
        return jsonify({'error': 'Ingen utleid bil funnet for denne kunden'}), 404

    car = find_car_by_id(order['car_id'])
    car['status'] = 'available'
    order['status'] = 'returnert'

    return jsonify({'message': 'Bil returnert', 'order': order}), 200

# Husk å importere denne filen og legge til blueprint i app.py























