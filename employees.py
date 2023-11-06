from flask import Blueprint, request, jsonify

employees_bp = Blueprint('employees', __name__)
employees = []

@employees_bp.route('/', methods=['POST'])
def create_employee():
    data = request.get_json()
    # Sjekk om den ansatte allerede eksisterer
    if any(employee['name'] == data['name'] and employee['address'] == data['address'] for employee in employees):
        return jsonify({'error': 'Den ansatte eksisterer allerede'}), 409

    employee = {
        'id': len(employees) + 1,
        'name': data['name'],
        'address': data['address'],
        'branch': data['branch']
    }
    employees.append(employee)
    return jsonify({'message': 'Ansatt opprettet', 'employee': employee}), 201

# ... (resten av endepunktene som de er i din eksisterende fil)




