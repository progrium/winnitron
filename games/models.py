from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    added = models.DateTimeField('date added')
    
    def serialize(self):
        return dict(
            name=self.name,
            description=self.description,
            category=self.category,
            developer=self.developer,
            added=self.added.strftime('%Y-%m-%dT%H:%M:%S')
        )