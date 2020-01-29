from django.urls import path
from .views import *

urlpatterns=[
    path('parlor/',view_get_post_parlor),
    path('parlor/<int:ID>',view_getByID_updateByID_deleteByID),
    path('parlor/<int:pageNo>/<int:items>',pagination)
]