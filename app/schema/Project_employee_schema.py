from marshmallow import Schema,fields
from app.models.project_employee import projectEmployee

class projectEmployeeSchema(Schema):
	emp_id = fields.Integer()
	project_id = fields.Integer()