from django.db import models

# Create your models here.
class Show(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField()
    url = models.URLField(max_length=50)
    date = models.CharField(max_length=30)
    time = models.DateTimeField()
    venue = models.TextField()
    artist = models.TextField()
    source = models.CharField(max_length=10)

    def __unicode__(self):
        return self.title
