from marshmallow import Schema,fields
from app.models.role import role

class roleSchema(Schema):
	role_id = fields.Integer(dump_only=True)
	name = fields.String()
	description = fields.String()