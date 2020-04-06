from django.db import models


# Create your models here.
class Client(models.Model):
    owner_ID = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=12, default=233, unique=True)
    email = models.EmailField(max_length=100)


    def __str__(self):
        return self.owner_ID
