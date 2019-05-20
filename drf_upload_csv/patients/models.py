from django.db import models


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
