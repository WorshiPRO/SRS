"""SRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from picksong.views import hello_view
from picksong.views import inputsong
from picksong.views import searchsong
from picksong.views import result
from picksong.views import all_result

urlpatterns = [
	path('', inputsong, name='index'),
    path('admin/', admin.site.urls),
	path('hello/', hello_view, name='hello'),
    path('inputsong/', inputsong, name='inputsong'),
    path('searchsong/', searchsong, name='searchsong'),
    path('result/', result, name='result'),
    path('all_result/', all_result, name='all_result'),
]
