# GitHub-RestAPI

Overview
	REST API for fetching GitHub Api data.
	Building in docker-compose (MongoDB+Python) and deploying on free linux AWS instance (t2.micro/EC2 service):
		http://ec2-3-92-229-25.compute-1.amazonaws.com:5000/
	In this case with ugly frontend :)
	Aslo project could be rebuild sepearately on localhost with nice frontend based on Jinja2/bootswatch style
		http://127.0.0.1:5000/

Features
	Overview top 10 stars list github repository
	Opportunity check detail info by git hub account login
	Overview all repository with stars rate over 2000 stars
	(Previously was 500, but when I published my Personal access tokens on git -
	I got the email "As a precautionary measure, we have revoked the OAuth token.
	A new token will need to be generated in order to continue using OAuth to authenticate to GitHub."
	I will resolve it in next version.)
	Use pagination per page when fetching github api data.

Installing
	1. run seperatly on localhost

		1.1. Make sure you have virtualenv and Python3 installed on your system (pip3 install virtualenv)
		1.2. Clone the repo: git clone https://github.com/vbondyrev/GitHub-RestAPI
		1.3. Install the virtualenv: virtualenv venv
		1.4. Activate the virtual environment: source venv/bin/activate
		1.5. Install Python Requirements: pip3 install -r requirements.txt
		1.6. Uncomment this row
			conn = MongoClient("mongodb://mongo:27017/", connect=False)              # PROD_ENV
			# conn = MongoClient("mongodb://localhost:27017/git_db", connect=False)  # DEV_ENV
		1.7. Run app.py and check this endpoint:
			http://127.0.0.1:5000/

	2. run inside docker-compose
	    2.1. Make sure you have docker-compose installed on your system
	    2.2. Clone the repo: git clone https://github.com/vbondyrev/GitHub-RestAPI
	    2.3. Run this script:
		 docker-compose -f docker-compose.yml up

Endpoints
	1. Start page with top 10 stars list github repository
		http://127.0.0.1:5000/
		http://127.0.0.1:5000/index

	2. 	Check detail info by git hub account login
		http://127.0.0.1:5000/user/<string:user_name>
		For example - my page:
		http://ec2-3-92-229-25.compute-1.amazonaws.com:5000/user/vbondyrev

	3. Save fetching result into mongodb
		http://127.0.0.1:5000/db/save

		(Pagination in this template in next version)

	4. Save fetching result into mongodb
		http://127.0.0.1:5000/db/save

	5. Delete collection in mongodb
		http://127.0.0.1:5000/db/del		


Underdeveloped on release version 1.3.0
	1. Pagination in template;
	2. Create unittest/pytest;
	3. Edit style this one Readme;
	4. Solve bug with Personal access tokens.

Thanks and have a nice day! :)
