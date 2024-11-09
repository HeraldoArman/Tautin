from django.urls import path
from tautin_app import views

url_list = {
    'dashboard' : "dashboard/",
    'register' : 'register/',
}

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(url_list['dashboard'], views.DashboardView.as_view(), name="dashboard"),
    path(url_list['register'], views.RegisterView.as_view(), name='register'),
    path('<str:short_url_link_address>/edit/', views.LinkEditView.as_view(), name='edit'),
    path('<str:short_url_link_address>/', views.redirect_to_long_link, name='redirect_to_long_link'),
    path('<str:short_url_link_address>/download', views.download_qr_code, name='download_qr'),
]
