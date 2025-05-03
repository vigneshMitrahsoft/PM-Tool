from flask import Flask
from views.techstack import app
from views.project import app

if __name__ == '__main__':
	app.run(debug=True)