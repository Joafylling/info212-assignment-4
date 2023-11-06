from flask import Blueprint, request, jsonify

customers_bp = Blueprint('customers', __name__)
customers = []

@customers_bp.route('/', methods=['POST'])
def create_customer():
    data = request.get_json()
    # Sjekk om kunden allerede eksisterer
    if any(customer['name'] == data['name'] and customer['address'] == data['address'] for customer in customers):
        return jsonify({'error': 'Kunden eksisterer allerede'}), 409

    customer = {
        'id': len(customers) + 1,
        'name': data['name'],
        'age': data['age'],
        'address': data['address']
    }
    customers.append(customer)
    return jsonify({'message': 'Kunde opprettet', 'customer': customer}), 201

# ... (resten av endepunktene som de er i din eksisterende fil)




