"""All Model definitions of patients app."""
from django.db import models


class User(models.Model):
    """Represents User class Model."""

    uuid = models.CharField(max_length=250)

    def __str__(self):
        """Return user uuid."""
        return self.uuid


class Patient(models.Model):
    """This Model represents a Patient class.

    :type firstname: string
    :param firstname: the firstname of the patient

    :type lastname: string
    :param lastname: the lastname of the patient

    :type email: string
    :param email: the email of the patient
    """

    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        """Return firstname and last name."""
        return " {}-{} ".format(self.firstname, self.lastname)


class FileUpload(models.Model):
    """Represents file upload model class."""

    owner = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    file = models.FileField(upload_to='csv_uploads/%y/%m')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return file name."""
        return self.file.name
