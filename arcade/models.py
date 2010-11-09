from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    screens_url = models.CharField(max_length=200)
    screens_updated = models.DateTimeField('date screens updated', null=True)
    download_url = models.CharField(max_length=200)
    download_updated = models.DateTimeField('date download updated', null=True)
    added = models.DateTimeField('date added', auto_now_add=True)
    tags = models.CharField(max_length=200)
    
    def save(self):
        self.tags = " %s " % ' '.join(filter(lambda x: x, self.tags.strip().split(' ')))
        super(Game, self).save()
    
    def tag_list(self):
        return filter(lambda x: x, self.tags.strip().split(' '))
    
    def __str__(self):
        return self.name
    
    def serialize(self):
        return dict(
            name=self.name,
            description=self.description,
            category=self.category,
            developer=self.developer,
            tags=self.tag_list(),
            screens_url=self.screens_url,
            screens_updated=self.screens_updated.strftime('%Y-%m-%dT%H:%M:%S') if self.screens_updated else None,
            download_url=self.download_url,
            download_updated=self.download_updated.strftime('%Y-%m-%dT%H:%M:%S') if self.download_updated else None,
            added=self.added.strftime('%Y-%m-%dT%H:%M:%S')
        )