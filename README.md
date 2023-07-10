# Drf File Upload

API allows a user to upload `.csv` & `xlsx` files containing patient names and emails then load the data into the database. Query Database and csv data with langchain.

Requirements:

```bash
Python >=3.0
Django==3.0
djangorestframework==3.14.0
pandas==2.0.3
langchain==0.0.229
openai
tabulate
```

## Features

- Uploading a file.

- Import works only for *.csv or *.xlsx files.

- Show error message if one tries to upload files in other formats.

- Show response when the import is done

- Show response if import wasn't done and the reason why.

- List all patients after the file has been uploaded.
- Query Database with LLM
- Query CSV with LLM

## Usage

Run:

`python manage.py makemigrations`

`python manage.py migrate`

### Create User

`python manage.py createsuperuser` follow prompt

### Making a POST request

&nbsp;
&nbsp;
![alt text](/static/postman01.PNG)

#### View the new data seeded

&nbsp;
&nbsp;
![alt text](/static/postman03.PNG)

#### TODO

- Show error message if the file is corrupted.

<!-- ### Clearing migrations

1. #### Remove the all migrations files within your project

Or if you are using a unix-like OS you can run the following script (inside your project dir):

```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete.

```

2. #### Drop the current database, or delete the db.sqlite3 if it is your case.

3. #### Create the initial migrations and generate the database schema

```bash
python manage.py makemigrations
python manage.py migrate
``` -->

#### Author

Philip Mutua
