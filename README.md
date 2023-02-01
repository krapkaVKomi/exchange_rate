Need to install: python 3.11 with pip, Postgresql (v.14)

Download project

In the folder with the project, you need to create a virtual environment
> mkdir myproject
> cd myproject
> py -3 -m venv venv

Activate virtual environment
> venv\Scripts\activate

Install packages 
> pip install -r requirements.txt

Need create new database in Postgresql 
with parameters password: postgres  port: 5432  name: rate  


Create and execute migrations
> flask db migrate

> flask db upgrade

Run project
> python app.py




