from django.db import models


class License(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField()


class Tag(models.Model):
    name = models.CharField(max_length=64)


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    url = models.URLField()
    license = models.ForeignKey(License)
    tags = models.ManyToManyField(Tag, related_name="projects+")

