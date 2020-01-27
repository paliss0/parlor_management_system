from django.db import models

# Create your models here.

#Models are for database. Parlor is table and content inside are column names in sql database
class Parlor(models.Model):
    parlor_name=models.TextField()
    parlor_description=models.TextField()
    address=models.TextField()
    price=models.IntegerField()



