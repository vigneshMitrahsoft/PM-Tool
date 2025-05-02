from marshmallow import Schema, fields
from models.techstackmodels import TechstackArea, TechStack

class TechstackAreaSchema(Schema):
    id = fields.Int(dump_only = True)
    tech_stack_area_name = fields.Str()

class TechStackSchema(Schema):
    id = fields.Int(dump_only = True)
    tech_name = fields.Str()
    tech_area_id = fields.Int()
