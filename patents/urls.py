from .views import archive_upload,delete_patent
from django.conf.urls import re_path

urlpatterns = [
    re_path('archive_upload/', archive_upload),
    re_path('delete_patent/', delete_patent)
]