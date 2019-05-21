"""Contains all the class views for patients app."""
import csv
import io
from .models import Patient
from .serializers import (
    PatientSerializer,
    FileSerializer
)
from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class FileUploadView(APIView):
    """Represents file upload view class.

    API endpoint that allows users to be upload a csv file.
    """

    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        """Upload the CSV file.

        Then reads it and saves csv data to database.

        """
        request.data['owner'] = request.user.id
        file_serializer = FileSerializer(data=request.data)
        # Commented code is for debugging only
        # import pdb; pdb.set_trace()
        # print(to_dict['_name'])
        _dict_file_obj = request.data['file'].__dict__
        if not _dict_file_obj['_name'].endswith('.csv'):
            return Response({"error": "Can only upload csv files"},
                            status=status.HTTP_BAD_REQUEST_400)

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_BAD_REQUEST_400)

        if file_serializer.is_valid():
            data = self.request.data.get('file')
            data_set = data.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            io_string = io.StringIO(data_set)
            next(io_string)

            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                obj, created = Patient.objects.get_or_create(
                    firstname=column[0],
                    lastname=column[1],
                    email=column[2]
                )
            file_serializer.save()
            return Response(
                {"message": "Upload Successfull",
                 "data": file_serializer.data}, status=200)
        else:
            return Response(file_serializer.errors, status=400)


class PatientListAPIView(generics.ListAPIView):
    """Class represents Patient API View.

    endpoint: /api/patients/list/

    GET: show list of patients.

    POST: create a patient.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
