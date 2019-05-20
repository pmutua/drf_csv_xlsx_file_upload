from django.db import models


class Patient(models.Model):
    """This Model represents a Patient class.

    :type name: string
    :param name: the name of the department
    """
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
