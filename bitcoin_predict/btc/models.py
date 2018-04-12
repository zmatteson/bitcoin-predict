from django.db import models
import datetime

# Create your models here.
class Price(models.Model):
    date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return str(self.date) + ' ' + str(self.price)
