# GitHub-RestAPI
Overview
	REST API 
	with docker-compose service(MongoDB+Python)

Requirements
	Python 3.4+
	VirtualEnv

Features
	Overview top 10 list github repository
	Overview all repository with stars rate over 500 stars
	Opportunity check datail info by git hub account login

Installing
	1. run seperatly without 
		1.1. istall all project dependencies 
			pip install -r requirements.txt
	
    1.1. Make sure you have virtualenv and Python3 installed on your system (pip3 install virtualenv)
    1.2. Clone the repo: git clone https://github.com/vbondyrev/GitHub-RestAPI
    1.3. Install the virtualenv: cd apisrv; virtualenv venv
    1.4. Activate the virtual environment: source venv/bin/activate
    1.5. Install Python Requirements: pip3 install -r requirements.txt
	
	2. run inside docker-compose
	    2.1. Make sure you have docker-compose installed on your system (pip3 install virtualenv)
		2.2. Run in the same folder
			docker-compose -f docker-compose.yml up
		2.3 Open on browser:
		

1. Add testing using unit-tests

Testing
http://flask.pocoo.org/docs/1.0/testing/
Example
https://stackoverflow.com/questions/41718376/how-to-apply-integration-tests-rather-than-unit-tests-to-a-flask-restful-api
https://stackoverflow.com/questions/28836893/how-to-send-requests-with-jsons-in-unit-tests
2. Upadate docher-copose file 
	and change Authentication to MongoDB (will use  /docker-entrypoint-initdb.d/*.js
Detаils here
https://docs.docker.com/samples/library/mongo/

3. Deploy this project on AWS (ES3) instance

4. Will add code for change environtment more simplify (Dev config/ Prod config)



As we can see from the code we have 2 GET requests and 1 POST request.

    Getting all data in the collection: 




















Developed:
-	Rest API architecture
    -	Ability to  view TOP Star repository
    -	Ability to view personal account with detail info
-	Flask fronted:
    -	 As template engine  Jinja2
    -	For style -  bootswatch.com – free themes
-	Logic working with MongoDB (save/read)
-	Full JSON support
-	Sorting by Star rank:
    -	Inside request query
    -	On template level, when show top repos 


Underdeveloped on release version 2.0
-	Pagination unresolved yet
-	Deatail README.md
-	Connection with Mongo DB service temporary  disabled, but code realized
    -   Trouble with MongoDB service  will solved in next api version
-	Dockerize application  and represent on AWS (ES3) instance

