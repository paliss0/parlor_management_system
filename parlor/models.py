from django.db import models
from django.contrib.auth.models import User

class Parlor(models.Model):
    parlor_logo=models.ImageField()
    parlor_name=models.TextField()
    parlor_description=models.TextField()
    address=models.TextField()
    price=models.IntegerField()

class ParlorUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.IntegerField()


class ParlorEmployee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.IntegerField()
    available_time=models.IntegerField()

class Appointment(models.Model):
    appointment_of=models.ManyToManyField(to=ParlorUser)
    appointment_for=models.ManyToManyField(to=ParlorEmployee)
    date=models.DateField(auto_now=True)









