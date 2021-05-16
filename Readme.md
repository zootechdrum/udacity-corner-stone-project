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
export FLASK_APP=app
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

## RBAC Roles
Due to time limitiations there are only 2 Roles 

* Executive Assistant

    The Executive assistant has the following permission
    1. ``` get:actors ```  The ability to looks at actors!
    2. ``` get movies ```  The ability to look at all the movies!


* Executive Director

    The Executive assistant has the following permission
    1. ``` get:actors ```  The ability to looks at actors!
    2. ``` get:movies ```  The ability to look at all the movies!
    3. ``` delete:actor```  The ability to delete a actor.
    4. ``` delete:movie```  The ability to delete a movie.
    5. ``` patch:actor```  The ability to update a actor.
    6. ``` patch:movie```  The ability to update a movie.
    7. ``` post:actor```  The ability to add an actor actor.
    8. ``` post:movie```  The ability to add a movie.

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

 ## DELETE /actors/<actor_id>
 
  * Returns a success message following a successful deletion of actor.
 ```
 {
   'success': True,
   'message': "Deleted an actor"
  }
 ```


 ## DELETE /movies/<movie_id>
 
  * Returns a success message following a successful deletion of Movie.
 ```
  {
   'success': True,
   'message': "Deleted a Movie"
  }
 ```

 ## Patch /actors/<int:actor_id>

  * Returns a success message following a successful update of an actor

  ```
  {
    'success': True,
     'message': "Updated actor successfuly"
  }
  ```

  ## Patch /movies/<int:id>

  * Returns a success message following a successful update of a Movie

  ```
  {
    'success': True,
    'message': "Updated movie successfuly"
  }
  ```
  # Executive Director Token: 
  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBxT0lFeU5nOEk5c2hHVG1KR2JDOSJ9.eyJpc3MiOiJodHRwczovL3pvb3RlY2hkcnVtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDQ1YTg1NDBkOWY3MTAwNzBlZTc5ODEiLCJhdWQiOlsiY29mZmUiLCJodHRwczovL3pvb3RlY2hkcnVtLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MjExMzI1NjIsImV4cCI6MTYyMTIxODk2MiwiYXpwIjoiQncxNWJTNjIxNVdjaWhyRUkwOXdWVm51RjJydDhhUUgiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.lr15Lh5WsYy1LwCpinXQf8BsfPJIkML6vNA4hi3tfBu3Mhw4Iun4w50w0bXd0Ag8YVoB3fk9KTt6jh8imnZNJgByLcGrxrKFJnt-vbQTJR8G_yZQdthIIMnlp7Tv48aeU7gbx6iMHvOhZlgUUwmMx_31NIAr933u89QSlsbR6K58jP2IDHA8CCvSqWtrUOdMVlzV-aS83aH4kRt1byjSPlCNbDOhu-Pv5eVQ9NFic_Nvg4K2TODfZQI40YL7_6fIyBGWVuIluFTCjaGpw9LQyR_3_LCkVTA7TfymhRPrT4anPdYXXknX3p2ZqEb_sLwOYA5YqHcDOR4t4K_DvBjgpQ


  # Executive Assistant
  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBxT0lFeU5nOEk5c2hHVG1KR2JDOSJ9.eyJpc3MiOiJodHRwczovL3pvb3RlY2hkcnVtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNDQ2MDUwMzYyNTYyMjA3MTQxMyIsImF1ZCI6WyJjb2ZmZSIsImh0dHBzOi8vem9vdGVjaGRydW0udXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMTEzMzQzMCwiZXhwIjoxNjIxMjE5ODMwLCJhenAiOiJCdzE1YlM2MjE1V2NpaHJFSTA5d1ZWbnVGMnJ0OGFRSCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.NzA1sjoi4u38EQsVCAWv_3PWlmGzYEUvXijzLLqNBSOvKkqLBcXTcmtAYwI46mxe8Oq4HLzNZbCy01U4IQaN1i6xR2XX-t_7HO6S9MUMRtL0YXjszBpi2p0goPCYmumeHSs0intADbD6ZD3FMcf0atfSVmtpaqQJ62gD9GJbAWBjSroHx99euX_p3lCvSm_H_C6GUGmaQ6f-3geLkeDY9SJpcGHo8SkCv24v8gVEVhA7fGD8BGuxeiUWCrbIakE5HPsbCTC1AroIrWx-gGYAjlB1ceSaW7xXaDjf65Smi3Sx6u5IFR-Yj9mpilhF1LxsxziV4T8HF4f-bT3VPBnqfg

 The deployed heroku application can be found [here](https://movie-casting.herokuapp.com/)






