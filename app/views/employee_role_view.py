from flask import request, jsonify, Flask, Blueprint
from config import session
from app.models.employee_role import employeeRole
from app.schema.employee_role_schema import employeeRoleSchema

employee_role_bp = Blueprint('employee_role_bp',__name__)

@employee_role_bp.route('/api/employee_role_create', methods=('POST',))
def employee_role():
	data = request.json
	new_emp = employeeRole(emp_id=data['emp_id'], role_id=data['role_id'])
	session.add(new_emp)
	session.commit()
	return jsonify(employeeRoleSchema().dump(new_emp))

@employee_role_bp.route('/api/employee_role_list', methods=('GET',))
def get_all():
	all_employee_role = session.query(employeeRole).all()
	return jsonify(employeeRoleSchema().dump(all_employee_role))

@employee_role_bp.route('/api/employee_role_list/<int:id>', methods=('GET',))
def get_one(id):
	get_employee_role = session.query(employee_role).get(id)
	return jsonify(employeeRoleSchema().dump(get_employee_role))

@employee_role_bp.route('/api/employee_role_update/<int:id>', methods=('PUT',))
def update(id):
	update_employee_role = session.query(employeeRole).get(id)
	data = request.json
	update_employee_role.emp_id = data.get('emp_id', update_employee_role.emp_id) 
	update_employee_role.role_id=data.get('role_id',update_employee_role.role_id)
	session.commit()
	return jsonify(employeeRoleSchema().dump(update_employee_role))

@employee_role_bp.route('/api/employee_role_delete/<int:id>', methods=('DELETE',))
def delete(id):
	delete_employee_role= session.query(employeeRole).get(id)
	session.delete(delete_employee_role)
	session.commit()
	return '',204