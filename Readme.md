# Movie Casting Agency

## Motivation for project
The motivation behind building this application is to further expand my knowledge in web development technologies. This project gave me the oppertunity to learn about Auth0, python, postman and SQLAlchemy. 

## Getting Started

### Installing Dependencies

python 3.7

Follow instructions to install the latest version of python for your platform in the python [Docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

Virtual Enviorment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python [docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:
```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the ```requirements.txt``` file.

Key Dependencies

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.
    * [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py  and can reference models.py.
    * [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.


## Running the server
From within the ```backend``` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Testing
To run the tests, run 
```
dropdb capstone_test
createdb capstone_test
python3 test_flaskr.py
```

## RBAC controls
Due to time limitiations there are only 2 users 

* Executive Assistant
* Executive Director

## API Reference

### Error Handling

Errors are returned as JSON objects in the following format

```
'success':False,
'error':404.
'message':'Resource Not Found'
```

The API will return four error types when requests fail:
* 404 Resources Not Found
* 422 Not Processable
* 405 Method Not Allowed
* 400 Bad Requests

# EndPoints

```
All of these endpoints require authorization headers
```

## GET /actors
 * Returns a list of actors that include data such as Gender, Full name, age.

 ```
 {
  "actors": [
    {
      "age": 25, 
      "gender": "Female", 
      "id": 26, 
      "name": "lus"
    }
  ], 
  "success": true
}
 ```

 ## GET /movies

 * Returns a list of movies that include data such as title of movie and the release date. 

 ```
 {
  "movies": [
    {
      "id": 22, 
      "release_date": "Sun, 25 Apr 2021 00:00:00 GMT", 
      "title": "cats"
    }, 
    {
      "id": 24, 
      "release_date": "Sun, 25 Apr 2021 00:00:00 GMT", 
      "title": "cats"
    }
  ], 
  "success": true
}
 ```

 ## Delete






