from flask import Flask
from app.views.company_views import main
from app.views.milestone_views import main
from app.views.timesheet_views import main

if __name__ == '__main__':
	main.run(debug = True)

 