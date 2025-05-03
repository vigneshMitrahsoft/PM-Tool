from flask import request, jsonify, Flask
from config import session
from app.models.role import Role
from app.schema.role_schema import roleschema
from flask_migrate import Migrate

app = Flask(__name__)
migrate = Migrate(app, session)

@app.route('/add_employee', methods=['POST'])
def add_employee():
	data = request.json
	new_role = Role(name=data['name'], description=data['description'])
	session.add(new_role)  
	session.commit()
	return jsonify(roleschema().dump(new_role))

@app.route('/', methods=['GET'])
def get_all():
	all_role = session.query(Role).all()
	return jsonify(roleschema().dump(all_role))

@app.route('/<int:id>', methods=['GET'])
def get_one(id):
	role = session.query(Role).get(id)
	return jsonify(roleschema().dump(role))

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
	role = session.query(Role).get(id)
	data = request.json
	role.name = data.get('name', role.name)
	role.description=data.get('description', role.description)
	session.commit()
	return jsonify(roleschema().dump(role))

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
	role = session.query(Role).get(id)
	session.delete(role)
	session.commit()
	return '',204
