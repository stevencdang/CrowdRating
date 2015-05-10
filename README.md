# CrowdRating
Flask/Heroku framework for performing crowd ratings using amazon mturk

## Requirements:
* Python 2.7
* Flask
* pip
* PyMongo
* Flask-Pymongo
* virtualenv
* Jquery 1.11.3
* skeljs 2.2.1


##Install Instructions:
To install you need to ensure python, virtualenv, pip, and heroku
toolbelt are installed. Starting from the base directory

Setup the virtual environment
```
$ virtualenv venv
```

Start to use the virtualenv by activating it (this must be done everytime you open a new terminal and you want to restart the webapp)
```
# source venv/bin/activate
```

Install the dependent packages using pip
```
$ pip install Flask gunicorn pymongo Flask-PyMongo
```

You can emulate a heroku stack to start the server easily as though it
is running on a heroku dyno
```
$ heroku login
Enter your Heroku credentials.
Email: kenneth@example.com
Password:

$ foreman start
```

## Running the application
There are 2 methods to run locally

1. Running a local Flask web-app container
2. Running a local heroku dyno container with Flask running


