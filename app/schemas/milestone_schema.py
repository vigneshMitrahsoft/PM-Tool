from app.models.milestone_models import milestone
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

class milestoneSchema(Schema):
    project_name = fields.String()
    planned_startdate = fields.Date()
    planned_enddate = fields.Date()
    actual_startdate = fields.Date()
    actual_enddate = fields.Date()
    status = fields.String()
    description = fields.String()
    
