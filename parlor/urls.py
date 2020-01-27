from django.urls import path
from .views import *

urlpatterns=[
    path('',get_parlor_home,name="parlor_home"),
    path('add-parlor/',get_add_parlor),
    path('update-parlor/<int:ID>/',get_update_parlor)
]