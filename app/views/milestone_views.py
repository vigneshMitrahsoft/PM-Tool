from flask import Flask, jsonify, request
from config import engine
from app.models.milestone_models import milestone
from sqlalchemy.orm import sessionmaker
from app.schemas.milestone_schema import milestoneSchema

Session = sessionmaker(bind = engine)
session = Session()

main = Flask(__name__)

@main.route('/milestone', methods = ('GET',))
def list_milestone():
	list_of_milestone = session.query(milestone).all()
	schema = milestoneSchema(many = True)
	result = schema.dump(list_of_milestone)
	return jsonify(result)

@main.route('/milestone/add', methods = ('POST',))
def add_milestone():
	data = request.json
	new_milestone = milestone(
		project_name = data['project_name'],
		planned_startdate = data['planned_startdate'],
		planned_enddate = data['planned_enddate'],
		actual_startdate = data['actual_startdate'],
		actual_enddate = data['actual_enddate'],
		status = data['status'],
		description = data['description'],
		created_by = "1",
	)
	session.add(new_milestone)
	session.commit()
	return jsonify(milestoneSchema().dump(new_milestone))

@main.route('/milestone/update/<int:milestone_id>', methods=('patch',))
def update_milestone(milestone_id):
	update_milestone = session.query(milestone).get(milestone_id)
	data = request.json
	update_milestone.project_name = data.get('project_name', update_milestone.project_name)
	update_milestone.planned_startdate = data.get('planned_startdate', update_milestone.planned_startdate)
	update_milestone.planned_enddate = data.get('planned_enddate', update_milestone.planned_enddate)
	update_milestone.actual_startdate = data.get('actual_startdate', update_milestone.actual_startdate)
	update_milestone.actual_enddate = data.get('actual_enddate', update_milestone.actual_enddate)
	update_milestone.status = data.get('status', update_milestone.status)
	update_milestone.description = data.get('description', update_milestone.description)
	update_milestone.updated_by = "2"
	session.commit()
	return jsonify(milestoneSchema().dump(update_milestone))

@main.route('/milestone/delete/<int:milestone_id>', methods = ('DELETE',))
def delete_company(milestone_id):
	user = session.query(milestone).get(milestone_id)
	session.delete(user)
	session.commit()
	return jsonify({'message' : 'successfully deleted'})