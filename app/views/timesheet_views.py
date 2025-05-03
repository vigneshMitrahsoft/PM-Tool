from flask import Flask, jsonify, request
from config import engine
from app.models.timesheet_models import timesheet
from sqlalchemy.orm import sessionmaker
from app.schemas.timesheet_schema import timesheetSchema

Session = sessionmaker(bind = engine)
session = Session()

main = Flask(__name__)

@main.route('/timesheet', methods = ('GET',))
def list_milestone():
	list_of_timesheet = session.query(timesheet).all()
	schema = timesheetSchema(many = True)
	result = schema.dump(list_of_timesheet)
	return jsonify(result)

@main.route('/timesheet/add', methods = ('POST',))
def add_timesheet():
	data = request.json
	timesheet_schema = timesheetSchema().load(data)
	new_timesheet = timesheet(
		task = timesheet_schema['task'],
		title = timesheet_schema['title'],
		description = timesheet_schema['description'],
		status = timesheet_schema['status'],
		created_by = "1",
	)
	session.add(new_timesheet)
	session.commit()
	return "created"

@main.route('/timesheet/update/<int:id>', methods = ('patch',))
def update_milestone(id):
	update_timesheet = session.query(timesheet).get(id)
	data = request.json
	timesheet_schema = timesheetSchema().load(data)
	update_timesheet.task = timesheet_schema.get('task', update_timesheet.task)
	update_timesheet.title = timesheet_schema.get('title', update_timesheet.title)
	update_timesheet.status = timesheet_schema.get('status', update_timesheet.status)
	update_timesheet.description = timesheet_schema.get('description', update_timesheet.description)
	update_timesheet.updated_by = "2"
	session.commit()
	return "updated"

@main.route('/timesheet/delete/<int:id>', methods = ('DELETE',))
def delete_company(id):
	user = session.query(timesheet).get(id)
	session.delete(user)
	session.commit()
	return jsonify({'message' : 'successfully deleted'})
