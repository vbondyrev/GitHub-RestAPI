# GitHub-RestAPI

REST API for fetching GitHub Api data.
### Overview
  * Building in docker-compose (MongoDB+Python) and deploying on free linux AWS instance (t2.micro/EC2 service):  
[http://ec2-52-207-234-223.compute-1.amazonaws.com:5000/](http://ec2-52-207-234-223.compute-1.amazonaws.com:5000/)
  * Aslo project could be rebuild sepearately on localhost:
		[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
  * Support memory object caching system - [memcached](https://hub.docker.com/_/memcached) with 5 min timeout
  
### Features
* Overview top 10 stars list github repository
* Opportunity check detail info by git hub account login
* Use pagination per page when fetching github api data.
* Overview all repository with stars rate over 10000 stars.  

### Installing
1. __Run seperatly on localhost__
* 1.1. Make sure you have virtualenv and Python3 installed on your system 
```
pip3 install virtualenv
```
* 1.2. Clone the repo: 
```
git clone https://github.com/vbondyrev/GitHub-RestAPI
```
* 1.3. Install the virtualenv: virtualenv venv
* 1.4. Activate the virtual environment: 
```
source venv/bin/activate
```
* 1.5. Install Python Requirements: 
```
pip3 install -r requirements.txt 
```
* 1.6. Uncomment this row:
```
conn = MongoClient("mongodb://localhost:27017/git_db", connect=False)  # DEV_ENV
```
* 1.7. Run app.py and check this endpoint:
			[http://127.0.0.1:5000/](http://127.0.0.1:5000/) 

2. __Run inside docker-compose__
* 2.1. Make sure you have docker-compose installed on your system
* 2.2. Clone the repo:
```
git clone https://github.com/vbondyrev/GitHub-RestAPI
```
* 2.3. From folder with project run this script:
```
docker-compose -f docker-compose.yml up
```
### Endpoints
 All endpoints published via Postman requests:
 * [https://documenter.getpostman.com/view/5674149/S11GSLAh](https://documenter.getpostman.com/view/5674149/S11GSLAh)
### Future developments
 * [See TODO.md](https://github.com/vbondyrev/GitHub-RestAPI/blob/master/TODO.md)
 
 _Thanks for attention and have a nice day! :)_
