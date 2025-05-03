from app.models.timesheet_models import timesheet
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

class timesheetSchema(Schema):
    task = fields.String()
    title = fields.String()
    description = fields.String()
    hours = fields.DateTime()
    status = fields.String()
    
    
