from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    url = models.URLField(blank=True)
    
    def __str__(self):  #functions in a model doesn't affect databse, so no need of migrating the changes
        return self.title