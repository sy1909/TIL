from django.urls import path
from bbsApp import views

urlpatterns = [
    path('index/' , views.index)
]