import datetime
from django.db import models
from app.models import Author


class Project(models.Model):
    name = models.CharField(max_length=64)
    repo_link = models.URLField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class ToDo(models.Model):
    for_project = models.ManyToManyField(Project)
    note_text = models.TextField()
    create_date = models.DateTimeField(datetime.datetime)
    update_date = models.DateTimeField(datetime.datetime.now())
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    condition = models.BooleanField(default=True)


