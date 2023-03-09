from app1.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('leo/',leo,name='leo'),
    path('rolex/',rolex,name='rolex'),
    path('vikram/',vikram,name='vikram0'),
]