from app2.views import *
from django.urls import path
app_name='smoker'
urlpatterns=[
    path('santhaanam/',santhaanam,name='santhaanam'),
    path('amar/',amar,name='amar'),
    path('vikram/',vikram,name='vikram'),
]