from flask import Flask, jsonify, request, Blueprint
from config import engine
from app.models.company import company
from sqlalchemy.orm import sessionmaker
from app.schemas.company import companySchema

Session = sessionmaker(bind = engine)
session = Session()

company_bp = Blueprint('company_bp', __name__)

@company_bp.route('/api/company', methods = ('GET',))
def list_company():
	list_of_company = session.query(company).all()
	schema = companySchema(many = True)
	result = schema.dump(list_of_company)
	return jsonify(result)

@company_bp.route('/api/create_company', methods = ('POST',))
def add_company():
	data = request.json
	company_schema = companySchema().load(data)
	new_company = company(
		company_name = company_schema['company_name'],
		address = company_schema['address'],
		phone_no = company_schema['phone_no'],
		email_id = company_schema['email_id'],
		is_active = company_schema.get('is_active', True),
		created_by = 1,
	)
	session.add(new_company)
	session.commit()
	return "created"

@company_bp.route('/api/update_company/<int:id>', methods = ('PATCH',))
def update_company(id):
	update_company = session.query(company).get(id)
	data = request.json
	company_schema = companySchema().load(data)
	update_company.company_name = company_schema.get('company_name', update_company.company_name)
	update_company.address = company_schema.get('address', update_company.address)
	update_company.phone_no = company_schema.get('phone_no', update_company.phone_no)
	update_company.email_id = company_schema.get('email_id', update_company.email_id)
	update_company.is_active = company_schema.get('is_active', update_company.is_active)
	update_company.updated_by = "2"
	session.commit()
	return jsonify({'message' : 'successfully updated'})

@company_bp.route('/api/delete_company/<int:id>', methods = ('DELETE',))
def delete_company(id):
	user = session.query(company).get(id)
	session.delete(user)
	session.commit()
	return jsonify({'message' : 'successfully deleted'})