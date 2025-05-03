from marshmallow import Schema,fields
from app.models.Employee_role import Employee_role

class employee_role_schema(Schema):
	emp_id = fields.Integer()
	role_id = fields.Integer()