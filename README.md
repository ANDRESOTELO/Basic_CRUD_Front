# Izeven technical test
For this technical test, I have been asked to create a web application with which the user can interact with a database, perform basic interactions (CRUD) with some of the tables and display information from some of the tables in the browser. 
# Technologies
For the backend:
- Python
- Flask
- Jinja2
- MySQL

For the frontend:
- HTML
- CSS
- Bootstrap

## Virtual environment
To install virtualenv
```
sudo pip3 install virtualenv
```
To create a new virtual environment with Python 3.7
```
virtualenv venv python=python3.7
```
Activate vitual environment

    source venv/bin/activate

## Virtual environment Configuration
Please run:

    (venv)$ pip3 install -r requirements.txt

Now we have to create environment variables

    (venv)$ export FLASK_APP=main.py
    (venv)$ export FLASK_DEBUG=1
    (venv)$ export FLASK_ENV=development

## DataBase
If you don´t have MySQL please install it first.

To setup the database

Please use the ***setup_mysql_dev.sql*** script and run:

    (venv)$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
Then to access to the DB:

    (venv)$ mysql -h localhost -u izeven_dev -p

## Run server

To run server:

    (venv)$ flask run
 
 Open the browser at:
 

> http://127.0.0.1:5000/ or http://localhost:5000/

## Interact with the App

You can select any of the buttons to interact with the database, enter students, create courses, create classes and upload student grades. 

> http://localhost:5000/

You can also edit or delete student records only with a button.

> http://localhost:5000/students/list


## Author

Andrés Sotelo | Software Developer 
- [LinkedIn] (https://www.linkedin.com/in/andresotelo/)
- [Github] (https://github.com/ANDRESOTELO/izeven_test)
Bogotá | Colombia
