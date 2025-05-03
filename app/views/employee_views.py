from flask import request, jsonify, Flask
from config import session
from app.models.employee import Employee
from app.schema.employee_schema import employeeschema
from flask_migrate import Migrate


app = Flask(__name__)

migrate = Migrate(app, session)

@app.route('/add_employee', methods=['POST'])
def add_employee():
	data = request.json
	print("sdnfs",data)
	print("ff",type(data['company_id']))
	print("kshfjs",type(data['project_id']))
	new_emp = Employee(fname=data['fname'], lname=data['fname'], email=data['email'], company_id=data['company_id'],project_id=data['project_id'])
	# print()
	session.add(new_emp)
	session.commit()
	return jsonify(employeeschema().dump(new_emp))

@app.route('/', methods=['GET'])
def get_all():
	all_emps = session.query(Employee).all()
	return jsonify(employeeschema().dump(all_emps))

@app.route('/<int:id>', methods=['GET'])
def get_one(id):
	emp = session.query(Employee).get(id)
	return jsonify(employeeschema().dump(emp))

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
	emp = session.query(Employee).get(id)
	data = request.json
	emp.fname = data.get('fname', emp.fname)
	emp.lname  = data.get('lname', emp.lname)
	emp.email  = data.get('email', emp.email)
	emp.company_id = data.get('company_id', emp.company_id)
	emp.project_id = data.get('project_id', emp.project_id)
	session.commit()
	return jsonify(employeeschema().dump(emp))

@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
	emp = session.query(Employee).get(id)
	session.delete(emp)
	session.commit()
	return '',204
