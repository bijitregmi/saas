"""
URL configuration for saas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from .views import home_page, about_page, pw_protected_view, user_only_view
from auth.views import login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('login/', login_view, name='login'),
    path('register', register_view, name='register'),
    path('accounts/', include('allauth.urls')),
    path('protected_entry/', pw_protected_view, name='protected_entry'),
    path('user_only/', user_only_view),
    path('profiles/', include('profiles.urls')),
]
