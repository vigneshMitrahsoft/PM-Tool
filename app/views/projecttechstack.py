from models.projecttechstackmodels import ProjectTechStack
from config import engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify, Flask, request
from schemas.projecttechstackschema import ProjectTechStackSchema

Session = sessionmaker(bind = engine)
db = Session()

app = Flask(__name__)

@app.route('/projectstacks', methods = ('GET',))
def get_project_stack():
	projectstack = db.query(ProjectTechStack).all()
	schema = ProjectTechStackSchema(many=True)
	return jsonify(schema.dump(projectstack))

@app.route('/createprojectstack', methods = ('POST',))
def create_project_stack():
	data = request.json
	projectstack = ProjectTechStack(
		project_id =  data["project_id"],
		techstack_id = data["techstack_id"],
		created_by = '1'
    )
	db.add(projectstack)
	db.commit()
	return jsonify({"message" : "Created Successfully"})

@app.route('/updateprojectstack/<int:id>', methods = ('PUT',))
def update_project_stack(id):
	projectstack = db.query(ProjectTechStack).get(id)
	if not projectstack:
		return jsonify({"message" : "Id does not exist"})
	data = request.json
	schemas = ProjectTechStackSchema.load(data)
	projectstack.project_id = schemas.get('project_id', projectstack.project_id)
	projectstack.techstack_id = schemas.get('techstack_id', projectstack.techstack_id)
	projectstack.updated_by = '1'
	db.commit()
	return jsonify({"message" : "Updated Successfully"})

@app.route('/deletestack/<int:id>', methods = ('DELETE',))
def delete_stack(id):
	tech = db.query(ProjectTechStack).get(id)
	if not tech:
		return jsonify({"message" : "Id does not exist"})
	db.delete(tech)
	db.commit()
	return jsonify({"message" : "Deleted Successfully"})