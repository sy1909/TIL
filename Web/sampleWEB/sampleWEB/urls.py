"""sampleWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from sampleWEB  import views #views 를 새로 만들었으니 불러온다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/', views.index),
    path('loginForm/' , views.loginForm),
    path('test/' , views.test),
    path('index/' , views.index),
    path('blog/' , include('blogApp.urls')),
    path('bbs/' , include('bbsApp.urls') ),
    path('user/' , include('userApp.urls') )
]

# user 에서 reqeust (url) 를 보낼때 위의 path를 찾는다 있으면 그리로 연결
# path를 찾았으면 실제로 연결되는 views를 찾아야한다. admin.site.urls 부분
