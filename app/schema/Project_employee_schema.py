from marshmallow import Schema,fields
from app.models.Project_employee import Project_employee

class project_employee_schema(Schema):
	emp_id = fields.Integer()
	project_id = fields.Integer()