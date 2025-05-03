from marshmallow import Schema,fields
from app.models.employee import Employee

class employeeschema(Schema):
	emp_id = fields.Integer(dump_only=True)
	fname = fields.String()
	lname = fields.String()
	email = fields.String()
	company_id = fields.Integer()
	project_id = fields.Integer()