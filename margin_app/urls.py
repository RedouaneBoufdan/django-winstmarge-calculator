from django.urls import path
from . import views

urlpatterns = [
    path('', views.margin_calculator, name='margin_calculator'),
]