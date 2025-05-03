from flask import request, jsonify, Flask
from config import session
from app.models.Employee_role import Employee_role
from app.schema.Employee_role_schema import employee_role_schema
from flask_migrate import Migrate

app = Flask(__name__)
migrate = Migrate(app, session)

@app.route('/add_employee', methods=['POST'])
def employee_role():
	data = request.json
	new_emp = Employee_role(emp_id=data['emp_id'],  role_id=data['role_id'])
	session.add(new_emp)
	session.commit()
	return jsonify(employee_role_schema().dump(new_emp))

@app.route('/', methods=['GET'])
def get_all():
	all_ER = session.query(Employee_role).all()
	return jsonify(employee_role_schema().dump(all_ER))

@app.route('/<int:id>', methods=['GET'])
def get_one(id):
	ER = session.query(Employee_role).get(id)
	return jsonify(employee_role_schema().dump(ER))

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
	ER = session.query(Employee_role).get(id)
	data = request.json
	ER.emp_id=data.get('emp_id', ER.emp_id) 
	ER.role_id=data.get('role_id',ER.role_id)
	session.commit()
	return jsonify(employee_role_schema().dump(ER))

@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
	ER = session.query(Employee_role).get(id)
	session.delete(ER)
	session.commit()
	return '',204