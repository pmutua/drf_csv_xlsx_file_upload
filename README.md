# Drf Upload CSV

API allows a user to upload `.csv` file and load the data into the database.

Requirements:
```bash
Python >=3.4
Django >= 2.0,
django-rest-auth
djangorestframework >=3.0
```

# Features

- Uploading a file.

- Import working only for CSV files.

- Show error message if one tries to upload files in other formats.

- Show response when the import is done

- Show response if import wasn't done and the reason why.

- List all patients after the file has been uploaded.


# Usage 

1. Run:

`python manage.py makemigrations`

`python manage.py migrate`


2. Create User

`python manage.py createsuperuser` follow prompt


3. Login to this url with your credentials: `http://localhost:8000/rest-auth/login/`


# Making Requests with postman:

Open Postman navigate to `Authorization` and choose  `Basic Auth`

![alt text](/static/postman.PNG)


## Making a POST request

![alt text](/static/postman01.PNG)


### TODO 

- Show error message if the file is corrupted.



#### Author 

Philip Mutua 