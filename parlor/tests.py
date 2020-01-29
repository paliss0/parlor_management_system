from django.test import TestCase
from django.contrib.auth.models import User

from .models import Parlor,ParlorUser,Appointment,ParlorEmployee

class ModelTestCase(TestCase):

    def test_valid_price(self):
        parlor=Parlor.objects.create(parlor_name="XYZ",parlor_description="Very Good Parlor",address="Kathmandu",price=1500)
        parlor.save()
        self.assertTrue(parlor.valid_price())
    
    def test_valid_name(self):
       parlor=Parlor.objects.create(parlor_name="XYZ",parlor_description="Very Good Parlor",address="Kathmandu",price=1500)
       self.assertTrue(parlor.valid_name())
    
    def test_valid_phone(self):
        user=User.objects.create_user(username="ABC",email="abc@gmail.com",password="123456789")
        user.save()
        parlor_user=ParlorUser(user=user,address="ktm",phone=986015632)

        self.assertTrue(parlor_user.valid_phone())

    
    def test_count_appointments(self):
        user=User.objects.create_user(username="ABC",email="abc@gmail.com",password="123456789")
        emp_user=User.objects.create_user(username="ABCD",email="abc@gmail.com",password="123456789")

        user.save()
        emp_user.save()
        
        parlor_emp=ParlorEmployee(user=emp_user,address="ktm",phone=98605241,available_time="9-5")
        parlor_user=ParlorUser(user=user,address="ktm",phone=986015632)

        parlor_emp.save()
        parlor_user.save()


        appointment=Appointment()

        appointment.appointment_of.add(parlor_user)
        appointment.appointment_for.add(parlor_emp)

        self.assertEqual(parlor_emp.count_appointments(),1)
    
    def test_available_time(self):
        emp_user=User.objects.create_user(username="ABCD",email="abc@gmail.com",password="123456789")
        parlor_emp=ParlorEmployee(user=emp_user,address="ktm",phone=98605241,available_time="9-5")

        self.assertEqual(parlor_emp.get_available_time(),"9-5")



    
