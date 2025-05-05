from flask import request, jsonify, Flask, Blueprint
from config import session
from app.models.employee import employee
from app.schema.employee_schema import employeeSchema

employee_bp = Blueprint('employee_bp',__name__)

@employee_bp.route('/api/employee_create', methods=('POST',))
def add_employee():
	data = request.json
	new_emp = employee(fname=data['fname'], lname=data['fname'], email=data['email'], company_id=data['company_id'],project_id=data['project_id'])
	session.add(new_emp)
	session.commit()
	return jsonify(employeeSchema().dump(new_emp))

@employee_bp.route('/api/employee_list', methods=('GET',))
def get_all():
	all_emps = session.query(employee).all()
	return jsonify(employeeSchema().dump(all_emps))

@employee_bp.route('/api/employee_list/<int:id>', methods=('GET',))
def get_one(id):
	emp = session.query(employee).get(id)
	return jsonify(employeeSchema().dump(emp))

@employee_bp.route('/api/employee_update/<int:id>', methods=('PUT',))
def update(id):
	emp = session.query(employee).get(id)
	data = request.json
	emp.fname = data.get('fname', emp.fname)
	emp.lname  = data.get('lname', emp.lname)
	emp.email  = data.get('email', emp.email)
	emp.company_id = data.get('company_id', emp.company_id)
	emp.project_id = data.get('project_id', emp.project_id)
	session.commit()
	return jsonify(employeeSchema().dump(emp))

@employee_bp.route('/api/employee_delete/<int:id>', methods=('DELETE',))
def delete(id):
	emp = session.query(employee).get(id)
	session.delete(emp)
	session.commit()
	return '',204