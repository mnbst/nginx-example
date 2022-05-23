from django.db import models


class File(models.Model):
    attachment = models.FileField()
