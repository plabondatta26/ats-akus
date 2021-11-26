from django.urls import path
from .views import *

urlpatterns = [
    path('about/us/', AboutView.as_view(), name='AboutView'),
    path('portfolio/', PortfolioView.as_view(), name='PortfolioView'),
    path('contact/us/', ContactView.as_view(), name='ContactView'),
]
