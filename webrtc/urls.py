from django.urls import path
from . import views

urlpatterns = [
    path('', views.caller, name='caller'),
]
