from django.db import models

# Create your models here.
class city(models.Model):
    city_name = models.CharField(max_length=25)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = 'city'