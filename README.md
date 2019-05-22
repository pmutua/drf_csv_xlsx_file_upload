# Drf File Upload

API allows a user to upload `.csv` & `xlsx` files containing patient names and emails then load the data into the database.

Requirements:
```bash
Python >=3.0
Django >= 2.0,
django-rest-auth
djangorestframework >=3.0
pandas == 0.24.2
```

# Features

- Uploading a file.

- Import working only for *.csv or *.xlsx files.

- Show error message if one tries to upload files in other formats.

- Show response when the import is done

- Show response if import wasn't done and the reason why.

- List all patients after the file has been uploaded.


# Usage 

#### Run:

`python manage.py makemigrations`

`python manage.py migrate`


#### Create User

`python manage.py createsuperuser` follow prompt


#### Login to this url with your credentials: `http://localhost:8000/rest-auth/login/`


# Open Postman navigate to `Authorization` and choose  `Basic Auth`


![alt text](/static/postman.PNG)


# Making a POST request


![alt text](/static/postman01.PNG)


# View the new data seeded 

![alt text](/static/postman03.PNG)

### TODO 

- Show error message if the file is corrupted.



#### Author 

Philip Mutua 
