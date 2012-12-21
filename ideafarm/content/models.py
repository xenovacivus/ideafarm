from django.db import models

# Create your models here.

class User (models.Model):
    name = models.CharField (max_length=100)
    def __unicode__ (self):
        return self.name

class Concept (models.Model):
    title = models.CharField (max_length = 300)
    description = models.TextField ()
    users = models.ManyToManyField (User)
#    views = models.IntegerField ()
    votes = models.IntegerField ()
    # creation_date = models.DateTimeField ('creation date')
    def __unicode__ (self):
        return self.title

