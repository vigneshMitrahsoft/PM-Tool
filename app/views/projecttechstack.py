from models.projecttechstack import ProjectTechStack
from config import engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify, Flask, request, Blueprint
from schemas.projecttechstack import ProjectTechStackSchema

Session = sessionmaker(bind = engine)
db = Session()

projecttechstack_bp = Blueprint('projecttechstack_bp', __name__)

@projecttechstack_bp.route('/api/projectstacks_list', methods = ('GET',))
def get_project_stack():
	project_stack = db.query(ProjectTechStack).all()
	schema = ProjectTechStackSchema(many=True)
	return jsonify(schema.dump(project_stack))

@projecttechstack_bp.route('/api/create_projectstack', methods = ('POST',))
def create_project_stack():
	data = request.json
	schemas = ProjectTechStackSchema().load(data)
	project_stack = ProjectTechStack(
		project_id =  schemas["project_id"],
		techstack_id = schemas["techstack_id"],
		created_by = '1'
    )
	db.add(project_stack)
	db.commit()
	return jsonify({"message" : "Created Successfully"})

@projecttechstack_bp.route('/api/update_projectstack/<int:id>', methods = ('PUT',))
def update_project_stack(id):
	project_stack = db.query(ProjectTechStack).get(id)
	if not project_stack:
		return jsonify({"message" : "Id does not exist"})
	data = request.json
	schemas = ProjectTechStackSchema().load(data)
	project_stack.project_id = schemas.get('project_id', project_stack.project_id)
	project_stack.techstack_id = schemas.get('techstack_id', project_stack.techstack_id)
	project_stack.updated_by = '1'
	db.commit()
	return jsonify({"message" : "Updated Successfully"})

@projecttechstack_bp.route('/api/delete_projectstack/<int:id>', methods = ('DELETE',))
def delete_stack(id):
	project_stack = db.query(ProjectTechStack).get(id)
	if not project_stack:
		return jsonify({"message" : "Id does not exist"})
	db.delete(project_stack)
	db.commit()
	return jsonify({"message" : "Deleted Successfully"})