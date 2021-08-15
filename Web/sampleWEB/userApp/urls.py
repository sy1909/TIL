from django.urls import path
from userApp import views

urlpatterns = [
    path('index/' , views.index)
]