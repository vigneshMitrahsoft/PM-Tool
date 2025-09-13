from flask import Flask, jsonify, request
from config import engine
from app.models.company_models import company
from sqlalchemy.orm import sessionmaker
from app.schemas.company_schema import companySchema

Session = sessionmaker(bind = engine)
session = Session()

main = Flask(__name__)

@main.route('/company', methods = ['GET'])
def list_company():
	list_of_company = session.query(company).all()
	schema = companySchema(many = True)
	result = schema.dump(list_of_company)
	return jsonify(result)

@main.route('/company/add', methods = ['POST'])
def add_company():
	data = request.json
	print(data)
	new_company = company(
		company_name = data['company_name'],
		address = data['address'],
		phone_no = data['phone_no'],
		email_id = data['email_id'],
		is_active = data.get('is_active', True),
		created_by = 1,
	)
	print(new_company)
	session.add(new_company)
	session.commit()
	return jsonify(companySchema().dump(new_company))

@main.route('/company/update/<int:id>', methods=['patch'])
def update_company(id):
	update_company = session.query(company).get(id)
	data = request.json
	update_company.company_name = data.get('company_name', update_company.company_name)
	update_company.address = data.get('address', update_company.address)
	update_company.phone_no = data.get('phone_no', update_company.phone_no)
	update_company.email_id = data.get('email_id', update_company.email_id)
	update_company.is_active = data.get('is_active', update_company.is_active)
	update_company.updated_by = "2"
	session.commit()
	return jsonify(companySchema().dump(update_company))

@main.route('/company/delete/<int:id>', methods = ['DELETE'])
def delete_company(id):
	user = session.query(company).get(id)
	session.delete(user)
	session.commit()
	return jsonify({'message' : 'successfully deleted'})