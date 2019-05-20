from .models import *
from rest_framework import serializers


class PatientSerializer(serializers.Serializer):
    """Represents patient serializer class."""

    class Meta:
        model = Patient
        fields = '__all__'
