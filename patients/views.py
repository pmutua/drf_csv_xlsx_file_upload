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
import pandas as pd
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class FileUploadView(APIView):
    """Represents file upload view class.

    API endpoint that allows users to be upload a csv file.

    POST: upload file
    """

    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        """Upload the CSV file.

        Then reads it and saves csv data to database.

        Endpoint: /api/patients/csv_upload
        """
        request.data['owner'] = request.user.id
        file_serializer = FileSerializer(data=request.data)
        # Commented code is for debugging only
        # import pdb; pdb.set_trace()
        # print(to_dict['_name'])
        _dict_file_obj = request.data['file'].__dict__

        _csv = _dict_file_obj['_name'].endswith('.csv')
        print(_csv)
        _excel = _dict_file_obj['_name'].endswith('.xlsx')

        if _csv or _excel is False:
            err = {"error": "Can only upload *.csv or *.xlsx files"}
            return Response(data=err,
                            status=status.HTTP_400_BAD_REQUEST)

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        if file_serializer.is_valid():
            data = self.request.data.get('file')

            if _csv is True:
                data_set = data.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                io_string = io.StringIO(data_set)

                csv_file = pd.read_csv(io_string, low_memory=False)
                columns = list(csv_file.columns.values)
                column_length = len(columns)
                if column_length != 3:
                    err = {"message": "The Excel File must have 3 columns \
                    in the following order: FirstName LastName Email"}
                    return Response(data=err,
                                    status=status.HTTP_400_BAD_REQUEST
                                    )
                first_name, last_name, email = columns[0], columns[1], columns[2]
                for index, row in csv_file.iterrows():
                    obj, created = Patient.objects.get_or_create(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        email=row[email]
                    )

            if _excel is True:
                xl = pd.read_excel(data)
                columns = list(xl.columns.values)
                column_length = len(list(xl.columns.values))
                # Check if the file has three columns.
                if column_length != 3:
                    err = {"message": "The Excel File must have 3 columns:  FirstName LastName Email"}
                    return Response(data=err,
                                    status=status.HTTP_400_BAD_REQUEST
                                    )
                first_name, last_name, email = columns[0], columns[1], columns[2]

                for index, row in xl.iterrows():
                    obj, created = Patient.objects.get_or_create(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        email=row[email]
                    )
            file_serializer.save()
            return Response(
                {"message": "Upload Successfull",
                 "data": file_serializer.data}, status=200)
        else:
            return Response(file_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )


class PatientListAPIView(generics.ListAPIView):
    """Class represents Patient API View.

    endpoint: /api/patients/list/

    GET: show list of patients.

    POST: create a patient.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
