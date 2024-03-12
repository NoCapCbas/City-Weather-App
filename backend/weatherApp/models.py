from django.db import models

# Create your models here.
class City(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = 'locations'
