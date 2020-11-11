from django.db import models


# Create your models here.

class FileUploadHistory(models.Model):
    upload_date = models.DateTimeField()
    file_name = models.CharField(max_length=100)
    executed = models.BooleanField(default=False)


class PatentNer(models.Model):
    patent_id = models.CharField(blank=True,max_length=20)
    title = models.TextField()
    year = models.IntegerField()
    abstract = models.TextField(blank=True)
    default_entities = models.TextField(blank=True)
    custom_entities = models.TextField(blank=True)

    def __str__(self):
        return self.title
