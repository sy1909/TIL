from django.urls import path
from blogApp import views

urlpatterns = [
    path('index/' , views.index)
]