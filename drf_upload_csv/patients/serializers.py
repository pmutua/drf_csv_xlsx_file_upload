from rest_framework import serializers


class Patient(serializers.Serializer):
    """Represents patient serializer class."""

    class Meta:
        model = Patient
        fields = '__all__'
