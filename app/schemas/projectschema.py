from marshmallow import Schema, fields
from models.projectmodels import Project

class ProjectSchema(Schema):
	project_id = fields.Int(dump_only = True)
	project_name = fields.Str()
	budget = fields.Int()
	startdate = fields.Date()
	duedate = fields.Date()
