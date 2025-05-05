from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

class companySchema(Schema):
	company_name = fields.String()
	address = fields.String()
	phone_no = fields.String()
	email_id = fields.String()
	is_active = fields.Boolean()