"""Contains all the class views for patients app."""
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
from rest_framework.permissions import AllowAny
from patients.llm.langchain import queryDb, queryCSV


class QueryDBAPIView(APIView):
    def post(self, request):
        text = request.data.get('prompt')
   
        try:
            res= queryDb(text)
            
            return Response(res, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            
class QueryCSVAPIView(APIView):
    def post(self, request):
        text = request.data.get('prompt')
   
        try:
            res= queryCSV(text)
            
            return Response(res, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class FileUploadView(APIView):
    """Represents file upload view class.

    API endpoint that allows users to be upload a csv file.

    POST: upload file
    """

    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        """Upload the CSV file.

        Then reads it and saves csv data to database.

        Endpoint: /api/patients/file_upload/
        """
        # request.data['owner'] = request.user.id
        file_serializer = FileSerializer(data=request.data)
        # Commented code is for debugging only
        # import pdb; pdb.set_trace()
        # print(to_dict['_name'])
        _dict_file_obj = request.data['file'].__dict__

        _csv = _dict_file_obj['_name'].endswith('.csv')

        _excel = _dict_file_obj['_name'].endswith('.xlsx')

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

                first_name, last_name, email, location, age = columns[0], columns[1],\
                    columns[2], columns[3], columns[4]

                instances = [
                    Patient(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        email=row[email],
                        location=row[location],
                        age=row[age]
                    )

                    for index, row in csv_file.iterrows()
                ]

                Patient.objects.bulk_create(instances)

            elif _excel is True:
                xl = pd.read_excel(data)
                columns = list(xl.columns.values)
                first_name, last_name, email, location, age = columns[0], columns[1],\
                    columns[2], columns[3], columns[4]

                instances = [
                    Patient(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        email=row[email],
                        location=row[location],
                        age=row[age]
                    )

                    for index, row in xl.iterrows()
                ]

                Patient.objects.bulk_create(instances)

            else:
                return Response(data={"err": "Must be *.xlsx or *.csv File."},
                                status=status.HTTP_400_BAD_REQUEST
                                )

            file_serializer.save()
            return Response(
                {"message": "Upload Successfull",
                 "data": file_serializer.data}, status=status.HTTP_200_OK)
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
