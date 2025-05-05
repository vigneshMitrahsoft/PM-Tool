from flask import Flask
from app.views.company import company_bp
from app.views.milestone import milestone_bp
from app.views.timesheet import timesheet_bp

main = Flask(__name__)

main.register_blueprint(company_bp)
main.register_blueprint(milestone_bp)
main.register_blueprint(timesheet_bp)

if __name__ == '__main__':
	main.run(debug = True)