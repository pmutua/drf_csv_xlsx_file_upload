from django.contrib import admin

# Register your models here.
from import_export import resources
from .models import *


class PatientResource(resources.ModelResource):

    class Meta:
        model = Patient
