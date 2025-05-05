from marshmallow import schema,fields

class employeeschema(schema):
     emp_id = fields.Int(required=True)
     fname = fields.Str()
     lname = fields.Str()
     email = fields.Str()
     company_id = fields.Int()
     project_id = fields.Int()
    
