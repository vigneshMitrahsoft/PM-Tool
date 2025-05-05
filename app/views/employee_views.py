from flask import request, jsonify, Flask
from config import session
from app.models.employee import Employee
from app.schema.employee_schema import employeeschema


employee_schema = employeeschema()
employees_schema = employeeschema(many=True)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_employee():
    data = request.json
    new_emp = Employee(fname=data['fname'], lname=data['fname'], email=data['email'], company_id=data['company_id'])
    session.add(new_emp)
    session.commit()
    return jsonify(employee_schema().dump(new_emp))

@app.route('/', methods=['GET'])
def get_all():
    all_emps = session.query(Employee).all()
    return jsonify(employee_schema().dump(all_emps))

@app.route('/<int:id>', methods=['GET'])
def get_one(emp_id):
    emp = session.query(Employee).get(emp_id)
    return jsonify(employee_schema().dump(emp))

@app.route('/<int:id>', methods=['PUT'])
def update(emp_id):
    emp = session.query(Employee).get(emp_id)
    data = request.json
    emp.fname = data.get('fname', emp.fname)
    emp.lname  = data.get('lname', emp.lname)
    emp.email  = data.get('email', emp.email)
    emp.company_id = data.get('company_id', emp.company_id)
    emp.project_id = data.get('project_id', emp.project_id)
    session.commit()
    return jsonify(employee_schema().dump(emp))

@app.route('/<int:id>', methods=['DELETE'])
def delete(emp_id):
    emp = session.query(Employee).get(emp_id)
    session.delete(emp)
    session.commit()
    return '',204
