from marshmallow import Schema,fields
from app.models.role import Role

class roleschema(Schema):
	role_id = fields.Integer(dump_only=True)
	name = fields.String()
	description = fields.String()