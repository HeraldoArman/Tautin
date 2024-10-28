from django.urls import path
from tautin_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
