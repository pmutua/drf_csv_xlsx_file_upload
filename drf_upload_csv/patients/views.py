from .serializers import *
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        """Upload the CSV file.

        Then reads it and saves data to database.
        """
        file_obj = request.data['file']

        return Response(status=status.HTTP_200_OK)
