from distutils.command.upload import upload
from django.db import models
from django.db import connections

# Create your models here.

class commitInfo(models.Model):   
    commit_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    commitmsg = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "commit_information"

# class UploadImage(models.Model):
#     image_field = models.ImageField(upload="upload/")
#     class Meta:
#         pass