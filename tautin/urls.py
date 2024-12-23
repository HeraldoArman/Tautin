"""
URL configuration for tautin project.

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
from django.contrib.auth import views
from django.contrib.sites.models import Site


Site.objects.clear_cache()

url_list = {
    'admin' : 'admin/',
    'login' : 'login/',
    'logout' : 'logout/',
    'accounts' : 'accounts/',
}

urlpatterns = [
    path(url_list['admin'], admin.site.urls),
    path(url_list['login'], views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('login/', include('allauth.urls')),
    path(url_list['logout'], views.LogoutView.as_view(next_page='index'), name='logout'),
    path(url_list['accounts'], include('allauth.urls')),
    path('', include('tautin_app.urls')),
]
