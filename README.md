# simple DEDIS Project

project is made with:

- Django
- Htmx
- poetry for version managment
- nix for instalations


# Setup

- download the repo
- if you have [nix (package manager)](https://nix.dev/install-nix) you can just run the flake to get all of the dependencies, but for the plebs:
    - python `>=3.11`
    - poetry


# getting the things working

firstly run 
```
cp env .env
```
and edit the `.env` file to give the project all the required variables

then run 
```
poetry install
```
which will... install all of the dependencies for the project

After that, when you need to run the following code **only once**
```
poetry run migrate
poetry run python manage.py collectstatic
poetry run python manage.py createsuperuser
```
The last one will prompt you to create an admin, on your local dev database.


After that you just run
```
poetry run dev
```

to start the server. Any changes should get auto updated by the instance.
