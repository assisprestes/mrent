from django.urls import path
from .views import *

urlpatterns = [
    path('', contratados, name='contratados')
]