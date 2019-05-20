"""This file contains all serializers for patients app."""
from .models import (
    Patient,
    FileUpload
)

from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    """Represents patient serializer class."""

    class Meta:
        """Contains model & fields used by this serializer."""

        model = Patient
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    """Represents file upload serializer class."""

    class Meta:
        """Contains model & fields used by this serializer."""

        model = FileUpload
        fields = '__all__'
