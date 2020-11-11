from celery.task import Task

from .service import get_abstract, get_description
from .models import FileUploadHistory, PatentNer
import zipfile
import os
import shutil
import xml.etree.ElementTree as et
from .service import get_custom_entitites,get_general_entities
from .models import PatentNer


class CheckNers(Task):
    """Task To Persist Patent Details of Patent along with NERS from Inbuilt and Custom NER Models"""
    def run(self):
        files = FileUploadHistory.objects.filter(executed=False)

        try:
            shutil.rmtree('media/files')
        except FileNotFoundError:
            pass

        for f in files:
            with zipfile.ZipFile('media/' + f.file_name, 'r') as zip_ref:
                zip_ref.extractall('media/files')

        for filename in os.listdir('media/files'):
            patent = {}
            if filename.endswith(".xml"):

                tree = et.parse('media/files/' + filename)
                element = tree.findall('bibliographic-data/invention-title')
                patent['patent_id'] = filename.split('.')[0]
                patent['title'] = element[0].text
                element = tree.findall('bibliographic-data/publication-reference/document-id/date')
                patent['year'] = int(element[0].text[0:4])
                element = tree.findall('abstract/')
                abstract_data = get_abstract(element)
                element = tree.findall('description/')
                desc_data = get_description(element)
                text = abstract_data + " " + desc_data
                patent['abstract'] = abstract_data
                patent['default_entities'] = get_general_entities(text)
                patent['custom_entities'] = get_custom_entitites(text)
                p = PatentNer(**patent)
                p.save()





