from flask import Flask
from app.views.employee_role_view import employee_role_bp
from app.views.employee_views import employee_bp
from app.views.project_employee_view import project_employee_bp
from app.views.role_views import role_bp
app = Flask(__name__)

app.register_blueprint(employee_role_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(project_employee_bp)
app.register_blueprint(role_bp)

if __name__ == '__main__':
	app.run(debug=True)
