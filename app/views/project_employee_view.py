from flask import request, jsonify, Flask
from config import session
from app.models.Project_employee import Project_employee
from app.schema.Project_employee_schema import project_employee_schema
from flask_migrate import Migrate

app = Flask(__name__)

migrate = Migrate(app, session)

@app.route('/add_employee', methods=['POST'])
def employee_role():
	data = request.json
	project_employee = Project_employee(emp_id=data['emp_id'],  project_id=data['role_id'])
	session.add(project_employee)
	session.commit()
	return jsonify(project_employee_schema().dump(project_employee))

@app.route('/', methods=['GET'])
def get_all():
	all_project_employee = session.query(Project_employee).all()
	return jsonify(project_employee_schema().dump(all_project_employee))

@app.route('/<int:id>', methods=['GET'])
def get_one(id):
   project_employee = session.query(Project_employee).get(id)
   return jsonify(project_employee_schema().dump(project_employee))

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
   project_employee = session.query(Project_employee).get(id)
   data = request.json
   project_employee.emp_id=data.get('emp_id',project_employee.emp_id) 
   project_employee.role_id=data.get('role_id',project_employee.role_id)
   session.commit()
   return jsonify(project_employee_schema().dump(project_employee))

@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
	project_employee = session.query().get(id)
	session.delete(project_employee)
	session.commit()
	return '',204
