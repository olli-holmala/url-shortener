# URL Shortener service

## 1. Summary

This is Olli Holmala's submission for Enel-X's technical challenge for a URL shortener service.

The task had two requirements:
1. Expose a POST endpoint for creating a minified URL
2. Expose a GET endpoint for resolving the minified URL

Choice of technology stack and architechture were left open to the applicant.

## 2. Technology stack

The technology stack chosen was Python and its Flask microframework. These were chosen due to the scope and time constraints of the task.

Dockerfile and docker-compose.yml files also provided for Dockerized deployment.

sqlite3 selected due to its ease of use and it being already integrated in Python.

API spec is available under ./docs
## 3. Instructions

### Running
* With Docker, just run `docker-compose up`
* Alternatively for a local run:
  * Activate a Python virtualenv (tested with Python version 3.8.8)
  * `pip install -r requirements.txt`
  * Set environment variables
    * `export FLASK_APP=./app.py`
    * `export FLASK_ENV=development`
  * `python db_init.py`
  * `flask run`
* The endpoints will be available on:
  * POST http://localhost:5000/minified
  * GET http://localhost:5000/minified/{id}

### Testing

POST endpoint can be tested with `curl`:

`curl -X POST -H "Content-Type: application/json" -d @./testdata/example-request.json http://localhost:5000/minified`
 
GET endpoint similarly:

`curl -X GET http://localhost:5000/minified/{id}`