from flask import Flask
from views.techstack import app

if __name__ == '__main__':
	app.run(debug=True)