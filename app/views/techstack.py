from models.techstackmodels import TechstackArea, TechStack, engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify, Flask, request
from schemas.techstackschema import TechstackAreaSchema, TechStackSchema

Session = sessionmaker(bind = engine)
db = Session()

app = Flask(__name__)

@app.route('/areas', methods = ('GET',))
def get_areas():
	areas = db.query(TechstackArea).all()
	schema = TechstackAreaSchema(many=True)
	return jsonify(schema.dump(areas))

@app.route('/stacks', methods = ('GET',))
def get_stack():
	stacks = db.query(TechStack).all()
	schema = TechStackSchema(many=True)
	return jsonify(schema.dump(stacks))

@app.route('/createstack', methods = ('POST',))
def create_stack():
	data = request.json
	tech = TechStack(
		tech_name =  data["tech_name"],
		tech_area_id = data["tech_area_id"],
		created_by = '1'
    )
	db.add(tech)
	db.commit()
	return jsonify(TechStackSchema().dump(tech))

@app.route('/updatestack/<int:id>', methods = ('PUT',))
def update_stack(id):
	tech = db.query(TechStack).get(id)
	if not tech:
		return jsonify({"message" : "Id does not exist"})
	data = request.json
	tech.tech_name = data.get('tech_name', tech.tech_name)
	tech.tech_area_id = data.get('tech_area_id', tech.tech_area_id)
	tech.updated_by = '1'
	db.commit()
	return jsonify(TechStackSchema().dump(tech))

@app.route('/deletestack/<int:id>', methods = ('DELETE',))
def delete_stack(id):
	tech = db.query(TechStack).get(id)
	if not tech:
		return jsonify({"message" : "Id does not exist"})
	db.delete(tech)
	db.commit()
	return jsonify({"message" : "Deleted Successfully"})

