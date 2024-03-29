from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    body = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Skill(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, default="ted-ed-logo-featured.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    


class Tags(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    


class Messages(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    subject = models.CharField(max_length=500, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    


class Endorsements(models.Model):
    name = models.CharField(max_length=200, null=True)
    body = models.TextField()
    approved = models.BooleanField(default=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.body[0:50]
    



class Comments(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.body[0:50]
    




