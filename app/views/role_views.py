from flask import request, jsonify, Flask, Blueprint
from config import session
from app.models.role import role
from app.schema.role_schema import roleSchema

role_bp = Blueprint('role',__name__)

@role_bp.route('/api/role_create', methods=('POST',))
def add_employee():
	data = request.json
	new_role = role(name=data['name'], description=data['description'])
	session.add(new_role)  
	session.commit()
	return jsonify(roleSchema().dump(new_role))

@role_bp.route('/api/role_list', methods=('GET',))
def get_all():
	all_role = session.query(role).all()
	return jsonify(roleSchema().dump(all_role))

@role_bp.route('/api/role_list/<int:id>', methods=('GET',))
def get_one(id):
	role_get = session.query(role).get(id)
	return jsonify(roleSchema().dump(role_get))

@role_bp.route('/api/role_update/<int:id>', methods=('PUT',))
def update(id):
	role_update = session.query(role).get(id)
	data = request.json
	role_update.name = data.get('name', role_update.name)
	role_update.description=data.get('description', role_update.description)
	session.commit()
	return jsonify(roleSchema().dump(role))

@role_bp.route('/api/role_delete/<int:id>', methods=('DELETE',))
def delete(id):
	role_delete = session.query(role).get(id)
	session.delete(role_delete)
	session.commit()
	return '',204