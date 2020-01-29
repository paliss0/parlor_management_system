import django.urls import path

import .views import *

urlpatterns=[
    path('parlor/',view_get_post_parlor),
    path('parlor/<int:ID>',view_getByID_updateByID_deleteByID)
]