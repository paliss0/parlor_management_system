from django.db import models
from django.contrib.auth.models import User

class Parlor(models.Model):
    parlor_logo=models.ImageField(null=True)
    parlor_name=models.TextField()
    parlor_description=models.TextField()
    address=models.TextField()
    price=models.IntegerField()

    def valid_price(self):
        return self.price>0
    
    def valid_name(self):
        return self.parlor_name!=""

class ParlorUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    address=models.TextField()
    phone=models.IntegerField()

    def valid_phone(self):
        return self.phone>0


class ParlorEmployee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    address=models.TextField()
    phone=models.IntegerField()
    available_time=models.TextField()

    def count_appointments(self):
        return self.appointment_of.all().cout()
    
    def get_available_time(self):
        return self.available_time

class Appointment(models.Model):
    id=models.IntegerField(primary_key=True)
    appointment_of=models.ManyToManyField(to=ParlorUser)
    appointment_for=models.ManyToManyField(to=ParlorEmployee)
    date=models.DateField(auto_now=True)









