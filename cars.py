from flask import Blueprint, request, jsonify

cars_bp = Blueprint('cars', __name__)
cars = []

@cars_bp.route('/', methods=['POST'])
def add_car():
    data = request.get_json()
    # Sjekk om bilen allerede eksisterer
    if any(car['make'] == data['make'] and car['model'] == data['model'] and car['year'] == data['year'] for car in cars):
        return jsonify({'error': 'Bilen eksisterer allerede'}), 409

    car = {
        'id': len(cars) + 1,
        'make': data['make'],
        'model': data['model'],
        'year': data['year'],
        'location': data['location'],
        'status': 'available'
    }
    cars.append(car)
    return jsonify({'message': 'Bil lagt til', 'car': car}), 201

# ... (resten av endepunktene som de er i din eksisterende fil)




