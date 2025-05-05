from flask import Flask
from views.techstack import tech_stack_bp
from views.project import project_bp
from views.projecttechstack import projecttechstack_bp

app = Flask(__name__)

app.register_blueprint(tech_stack_bp)
app.register_blueprint(project_bp)
app.register_blueprint(projecttechstack_bp)

if __name__ == '__main__':
	app.run(debug=True)