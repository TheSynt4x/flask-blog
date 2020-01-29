# Flask Blog

A simple blog written in Flask.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Python 3.7 or later to run this project.

```
https://www.python.org/downloads/
```

### Installing

You will need to install pipenv on your machine. You will also need to install the dependencies that come with the project. 

Installing pipenv:

```
pip3 install pipenv
```

More details of pipenv and what it is can be found at: https://pipenv-fork.readthedocs.io/en/latest/

Installing the dependencies:
```
pipenv install
```

Running the project:
```
python app.py
```

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - ORM used to handle database actions
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - Used to handle forms and form validation
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) - Used to encrypt passwords

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
