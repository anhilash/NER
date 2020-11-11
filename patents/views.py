from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FileUploadHistory,PatentNer
from zipfile import is_zipfile
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from .service import to_datetime
import datetime
from .tasks import CheckNers
from rest_framework.generics import get_object_or_404


# Create your views here.

@api_view(['POST'])
def archive_upload(request):
    """ Archive Upload Endpoint"""
    archive = request.FILES.get('archive', None)

    if is_zipfile(archive):
        files = FileUploadHistory.objects.filter(file_name=archive.name)
        if files:
            res = {'File already uploaded'}
            return Response(res, status=status.HTTP_200_OK)
        else:
            filehistory_dict = {
                'upload_date': to_datetime(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
                'file_name': archive.name
            }

            '''Saving to file upload history'''

            fileupload_history = FileUploadHistory(**filehistory_dict)
            fileupload_history.save()
            fs = FileSystemStorage()
            filename = fs.save(archive.name, archive)
            res = {'File ' + filename + ' uploaded Successfully and started processing'}

            """ Calling Asynchronous Task for extracting the Details from uploaded archive """
            CheckNers.delay()
            return Response(res, status=status.HTTP_200_OK)

    else:
        res = {'message': 'Please check the file format'}
        return Response(res, status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
def delete_patent(request):
    patent_id = request.GET.get('patent_id', None)
    patent = get_object_or_404(PatentNer, patent_id=patent_id)
    if patent:
        patent.delete()
        res = {'message': 'Patent Deleted'}
        return Response(res, status=status.HTTP_200_OK)
    else:
        res = {'message': 'Patent Not Found'}
        return Response(res, status=status.HTTP_404_NOT_FOUND)


