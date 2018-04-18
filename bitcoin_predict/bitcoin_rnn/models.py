from django.db import models
# Create your models here.
import datetime

# Create your models here.
class FuturePrice(models.Model):
    date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return str(self.date) + ' ' + str(self.price)
