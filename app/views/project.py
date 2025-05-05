from models.project import Project
from config import engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify, request, Blueprint
from schemas.project import ProjectSchema

Session = sessionmaker(bind = engine)
db = Session()

project_bp = Blueprint('project_bp', __name__ )

@project_bp.route('/api/project_list', methods = ('GET',))
def get_projects():
	projects = db.query(Project).all()
	schema = ProjectSchema(many=True)
	return jsonify(schema.dump(projects))

@project_bp.route('/api/create_project', methods = ('POST',))
def create_project():
	data = request.json
	schemas = ProjectSchema().load(data)
	project = Project(
		project_name =  schemas["project_name"],
		budget = schemas["budget"],
		startdate = schemas["startdate"],
		duedate = schemas["duedate"],
		created_by = '1'
    )
	db.add(project)
	db.commit()
	return jsonify({"message" : "created successfully"})

@project_bp.route('/api/update_project/<int:id>', methods = ('PUT',))
def update_project(id):
	tech = db.query(Project).get(id)
	if not tech:
		return jsonify({"message" : "Id does not exist"})
	data = request.json
	schemas = ProjectSchema().load(data)
	tech.project_name = schemas.get('project_name', tech.project_name)
	tech.budget = schemas.get('budget', tech.budget)
	tech.startdate = schemas.get('startdate', tech.startdate)
	tech.updated_by = '1'
	db.commit()
	return jsonify({"message": "updated successfully"})

@project_bp.route('/api/delete_project/<int:id>', methods = ('DELETE',))
def delete_project(id):
	project = db.query(Project).get(id)
	if not project:
		return jsonify({"message" : "Id does not exist"})
	db.delete(project)
	db.commit()
	return jsonify({"message" : "Deleted Successfully"})
