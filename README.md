# Chem NER

Chem NER is a RESTFul based application to upload an archive of xml fies, which contains details of patents. And the application persists NERS based on inbuilt and custom model which is trained on the data provided. It contains two end point.

  - patents/archive_upload/
  - patents/delete_patent

### Tech

 Used a number of open source projects to work properly:

* [django_rest_framework] - Web frame work in python for building REST API's
* [redis] - Message Broker
* [celery] - Celery is an open source asynchronous task queue
* [Spacy] - Package for NLP
* [MongoDB] - Document Based DataBase

### Running 
Install the dependencies.

```sh
$ pip install -r requirements.txt
```
Start redis server...

```sh
$ redis-server
```
Check if redis is running or not..
```sh
$ redis-cli ping
```
Run celery..
```sh
$ celery -A NER worker -l info
```
Make sure the mongo DB is installed and configured accordingly in settings.py
```sh
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'DB_NAME',
    }
}
```
Make Migrations and Migrate..
```sh
$ python manage.py makemigrations
$ python namage.py migrate
```

Finally run the Server..
```sh
$ python manage.py runserver
```
# API's
### Archive Upload Request
HTTP VERB : POST
http://localhost:8000/patents/archive_upload/
In form-data pass:
    archive : zip_file
### Response
```sh
[
    "File uspat1_201831_back_80001_100000.zip uploaded Successfully and started processing"
]
```


### Delete Patents Details Request
HTTP VERB : DELETE
http://localhost:8000/patents/delete_patent/?patent_id=USD0437352S1

### Response
```sh
{
    "message": "Patent Deleted"
}
```



