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

![enter image description here](https://previews.dropbox.com/p/thumb/ABO1McNVZ76x3HTIhUfWLGGGQwkiYycwOXOKZ3kvRbRfjbNkchUwQ-ND1TH_4T3ynQzgxVIT3Vn3D5Oo6TsJ83f0JGHqcq2ZIDzx9a0Si9M9aHzK2231eBy4RrwIjFa1uhaVGbI-YSuD1Me3Vry8lYxP4gWOiuRVmBr8vCZ2Hb5jg-gBDymhf7YQw2SC1X2U8ZDSlJVFd3H6CP__pKh-H6kMpgPBDVsmJdflgbyKR6Uw6orXI1wzlYjSiSniuPVZiTQm73MzxYdi7iAZExOa_ljZhO5EtJe1SmVnC6u3b7BSB1XUY5hqkj3CBjyi45GC7yucE_4MXhZ8Aeldx0rh76fNqghDUqLH2B6_JKWkMvo13Q/p.png?fv_content=true&size_mode=5)

## Interact with the App

You can select any of the buttons to interact with the database, enter students, create courses, create classes and upload student grades. 

![enter image description here](https://previews.dropbox.com/p/thumb/ABOybp_PjIijpW_EBpFYfXXHZJI32oDqgjmiL0B53KgpLpRafjkSA9wl9v0tBDCMakhbfj8Fe4g4GDZchUttsorbGCW2uR0oTjc38gWl1yY5K7mnSePYfvfYjiv2xpp7KII-NWE3Yf7Cit5NN2xPO4P57Y0bvPGO33x1-xj7KrJatb4Nr6ieb9TF2_h-JdqlEQ-d1c45TsAUP8RANCWBsuf1re5pU6nqfQJIKx7wyT4h04mJ_-QZctQrHWrNM2FRW0_MBbi2WPN7lZWZnv8l5Pq7JUWygHtVvVmLfV-3wCrzTkT8aGnJOLwObN6sQLWzDd9TFeW-UfvEca5NirJ8SoxacjcLfvOYYTdmL9wfVTrYKA/p.png?fv_content=true&size_mode=5)

You can also edit or delete student records only with a button.

![enter image description here](https://previews.dropbox.com/p/thumb/ABMe8cV4HpjpQKLoq_KZ-jId_gPnniz8uDe44EUi757yMgzAJNk1rM-iuZk1t-5xKHkfG9iNdkC70u-mtyhVcLlBbeDVrkpWD_2FnY4YdFjvlvWqnLD9TOplGeEtArkHYKCALFnk6E-AJkNup_IrU44YprRMNlw6kC3kHWz-Q9xTsVHb8o_SjUimeW2XFwwAATYrCiUu8kqzE3PhgEJxkZB0MFoxJf8icJnrV4OtWy0nQUlhax5NNHjfhCR3FMlwI3RqkVFsf5x8vJ2sSFJ8vAJnZ7j3chXHZg49L-v5XhORiGTLXtLzsaTZjLJHP0Ekbjfo8DqBRwJJ7CRSdOkqsqYjD99lkrxOzYOJrf-c1WGLlQ/p.png?fv_content=true&size_mode=5)


## Author

Andrés Sotelo | Software Developer 
- [LinkedIn] (https://www.linkedin.com/in/andresotelo/)
- [Github] (https://github.com/ANDRESOTELO/izeven_test)
Bogotá | Colombia
