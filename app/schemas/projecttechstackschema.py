from marshmallow import Schema, fields

class ProjectTechStackSchema(Schema):
	id = fields.Int(dump_only = True)
	project_id = fields.Int()
	techstack_id = fields.Int()
	

