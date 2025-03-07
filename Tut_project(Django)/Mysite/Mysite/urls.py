"""
URL configuration for Mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),  # Home page URL
    path('about/', views.About, name='about'),  # About page URL
    path('shop/', views.Shop, name='shop'),  # Shop page URL
    path('contact/', views.Contact, name='contact'),  # Contact page URL
    path('chat/', views.Chat, name='chat'),  # Chat page URL
]
