from django.urls import path, include
from .views import *

urlpatterns = [
    path('services/', ServiceView.as_view(), name='ServiceView'),
    path('blogs/', BlogView.as_view(), name='BlogView'),
]
