from marshmallow import Schema,fields
from app.models.employee_role import employeeRole

class employeeRoleSchema(Schema):
	emp_id = fields.Integer()
	role_id = fields.Integer()