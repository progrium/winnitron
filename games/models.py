from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    added = models.DateTimeField('date added')
