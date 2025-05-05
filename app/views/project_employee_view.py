from flask import request, jsonify, Flask, Blueprint
from config import session
from app.models.project_employee import projectEmployee
from app.schema.project_employee_schema import projectEmployeeSchema

project_employee_bp = Blueprint('Project_employee_bp',__name__)

@project_employee_bp.route('/api/project_employee_create', methods=('POST',))
def employee_role():
	data = request.json
	project_employee = projectEmployee(emp_id=data['emp_id'],  project_id=data['project_id'])
	session.add(project_employee)
	session.commit()
	return jsonify(projectEmployeeSchema().dump(project_employee))

@project_employee_bp.route('/api/project_employee_list', methods=('GET',))
def get_all():
	all_project_employee = session.query(projectEmployee).all()
	return jsonify(projectEmployeeSchema().dump(all_project_employee))

@project_employee_bp.route('/api/project_employee_list/<int:id>', methods=('GET',))
def get_one(id):
   project_employee = session.query(projectEmployee).get(id)
   return jsonify(projectEmployeeSchema().dump(project_employee))

@project_employee_bp.route('/api/project_employee_update/<int:id>', methods=('PUT',))
def update(id):
   project_employee = session.query(projectEmployee).get(id)
   data = request.json
   project_employee.emp_id=data.get('emp_id',project_employee.emp_id) 
   project_employee.role_id=data.get('role_id',project_employee.role_id)
   session.commit()
   return jsonify(projectEmployeeSchema().dump(project_employee))

@project_employee_bp.route('/api/project_employee_delete/<int:id>', methods=('DELETE',))
def delete(id):
	project_employee_delete = session.query(projectEmployee).get(id)
	session.delete(project_employee_delete)
	session.commit()
	return '',204